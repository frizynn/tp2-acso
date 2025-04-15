; /** defines bool y puntero **/
%define NULL 0
%define TRUE 1
%define FALSE 0

section .data

section .text

global string_proc_list_create_asm
global string_proc_node_create_asm
global string_proc_list_add_node_asm
global string_proc_list_concat_asm

; FUNCIONES auxiliares que pueden llegar a necesitar:
extern malloc
extern free
extern str_concat
extern strlen
extern strcpy

; --- Auxiliar: inicializa dos punteros a NULL en una struct de 16 bytes ---
init_list_struct:
        mov     QWORD [rax], 0
        mov     QWORD [rax+8], 0
        ret

; --- Auxiliar: inicializa nodo de 32 bytes (type, hash, next, prev) ---
init_node_struct:
        movzx   edx, BYTE [rbp-20]
        mov     BYTE [rax+16], dl
        mov     rdx, QWORD [rbp-32]
        mov     QWORD [rax+24], rdx
        mov     QWORD [rax], 0
        mov     QWORD [rax+8], 0
        ret

; --- Auxiliar: retorna 0 y sale ---
return_null:
        mov     eax, 0
        leave
        ret

string_proc_list_create_asm:
        push    rbp
        mov     rbp, rsp
        sub     rsp, 16
        mov     edi, 16
        call    malloc
        mov     QWORD [rbp-8], rax
        cmp     QWORD [rbp-8], 0
        je      return_null
        mov     rax, QWORD [rbp-8]
        call    init_list_struct
        mov     rax, QWORD [rbp-8]
        leave
        ret

string_proc_node_create_asm:
        push    rbp
        mov     rbp, rsp
        sub     rsp, 32
        mov     eax, edi
        mov     QWORD [rbp-32], rsi
        mov     BYTE [rbp-20], al
        cmp     QWORD [rbp-32], 0
        je      return_null
        mov     edi, 32
        call    malloc
        mov     QWORD [rbp-8], rax
        cmp     QWORD [rbp-8], 0
        je      return_null
        mov     rax, QWORD [rbp-8]
        call    init_node_struct
        mov     rax, QWORD [rbp-8]
        leave
        ret

string_proc_list_add_node_asm:
        push    rbp
        mov     rbp, rsp
        sub     rsp, 48
        mov     QWORD [rbp-24], rdi
        mov     eax, esi
        mov     QWORD [rbp-40], rdx
        mov     BYTE [rbp-28], al
        cmp     QWORD [rbp-24], 0
        je      .end
        cmp     QWORD [rbp-40], 0
        je      .end
        movzx   eax, BYTE [rbp-28]
        mov     rdx, QWORD [rbp-40]
        mov     rsi, rdx
        mov     edi, eax
        call    string_proc_node_create_asm
        mov     QWORD [rbp-8], rax
        cmp     QWORD [rbp-8], 0
        je      .end
        mov     rax, QWORD [rbp-24]
        mov     rax, QWORD [rax]
        test    rax, rax
        jne     .not_empty
        mov     rax, QWORD [rbp-24]
        mov     rdx, QWORD [rbp-8]
        mov     QWORD [rax], rdx
        mov     rax, QWORD [rbp-24]
        mov     rdx, QWORD [rbp-8]
        mov     QWORD [rax+8], rdx
        jmp     .end
.not_empty:
        mov     rax, QWORD [rbp-24]
        mov     rdx, QWORD [rax+8]
        mov     rax, QWORD [rbp-8]
        mov     QWORD [rax+8], rdx
        mov     rax, QWORD [rbp-24]
        mov     rax, QWORD [rax+8]
        mov     rdx, QWORD [rbp-8]
        mov     QWORD [rax], rdx
        mov     rax, QWORD [rbp-24]
        mov     rdx, QWORD [rbp-8]
        mov     QWORD [rax+8], rdx
.end:
        leave
        ret

string_proc_list_concat_asm:
        push    rbp
        mov     rbp, rsp
        sub     rsp, 64
        mov     QWORD [rbp-40], rdi
        mov     eax, esi
        mov     QWORD [rbp-56], rdx
        mov     BYTE [rbp-44], al
        cmp     QWORD [rbp-40], 0
        je      .ret_null
        cmp     QWORD [rbp-56], 0
        je      .ret_null
        mov     rax, QWORD [rbp-56]
        mov     rdi, rax
        call    strlen
        mov     QWORD [rbp-24], rax
        mov     rax, QWORD [rbp-24]
        add     rax, 1
        mov     rdi, rax
        call    malloc
        mov     QWORD [rbp-8], rax
        cmp     QWORD [rbp-8], 0
        je      .ret_null
        mov     rdx, QWORD [rbp-56]
        mov     rax, QWORD [rbp-8]
        mov     rsi, rdx
        mov     rdi, rax
        call    strcpy
        mov     rax, QWORD [rbp-40]
        mov     rax, QWORD [rax]
        mov     QWORD [rbp-16], rax
        jmp     .loop_cond
.loop:
        mov     rax, QWORD [rbp-16]
        movzx   eax, BYTE [rax+16]
        cmp     BYTE [rbp-44], al
        jne     .next
        mov     rax, QWORD [rbp-16]
        mov     rax, QWORD [rax+24]
        test    rax, rax
        je      .next
        mov     rax, QWORD [rbp-16]
        mov     rdx, QWORD [rax+24]
        mov     rax, QWORD [rbp-8]
        mov     rsi, rdx
        mov     rdi, rax
        call    str_concat
        mov     QWORD [rbp-32], rax
        cmp     QWORD [rbp-32], 0
        jne     .concat_ok
        mov     rax, QWORD [rbp-8]
        jmp     .ret
.concat_ok:
        mov     rax, QWORD [rbp-8]
        mov     rdi, rax
        call    free
        mov     rax, QWORD [rbp-32]
        mov     QWORD [rbp-8], rax
.next:
        mov     rax, QWORD [rbp-16]
        mov     rax, QWORD [rax]
        mov     QWORD [rbp-16], rax
.loop_cond:
        cmp     QWORD [rbp-16], 0
        jne     .loop
        mov     rax, QWORD [rbp-8]
        jmp     .ret
.ret_null:
        mov     eax, 0
.ret:
        leave
        ret
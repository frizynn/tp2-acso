#include "ej1.h"

/**
 * Crea una nueva lista enlazada vacía.
 * 
 * @return Puntero a la nueva lista o NULL si falló la asignación de memoria.
 */
string_proc_list* string_proc_list_create(void) {
    string_proc_list* list = (string_proc_list*)malloc(sizeof(string_proc_list));
    if (list == NULL) {
        return NULL;
    }
    
    list->first = NULL;
    list->last = NULL;
    
    return list;
}

/**
 * Crea un nuevo nodo con el tipo y hash especificados.
 *
 * @param type El tipo del nodo.
 * @param hash Puntero al hash (no se copia).
 * @return Puntero al nuevo nodo o NULL si falló la asignación de memoria o hash es NULL.
 */
string_proc_node* string_proc_node_create(uint8_t type, char* hash) {
    if (hash == NULL) {
        return NULL;
    }
    
    string_proc_node* node = (string_proc_node*)malloc(sizeof(string_proc_node));
    if (node == NULL) {
        return NULL;
    }
    
    node->type = type;
    node->hash = hash;  // No copiamos el hash, apuntamos al mismo
    node->next = NULL;
    node->previous = NULL;
    
    return node;
}

/**
 * Agrega un nuevo nodo al final de la lista con el tipo y hash especificados.
 *
 * @param list Puntero a la lista.
 * @param type El tipo del nodo a agregar.
 * @param hash Puntero al hash (no se copia).
 */
void string_proc_list_add_node(string_proc_list* list, uint8_t type, char* hash) {
    if (list == NULL || hash == NULL) {
        return;
    }
    
    string_proc_node* new_node = string_proc_node_create(type, hash);
    if (new_node == NULL) {
        return;
    }
    
    if (list->first == NULL) {
        // Lista vacía
        list->first = new_node;
        list->last = new_node;
    } else {
        // Agregar al final
        new_node->previous = list->last;
        list->last->next = new_node;
        list->last = new_node;
    }
}

/**
 * Concatena el hash dado con los hashes de todos los nodos del tipo especificado.
 *
 * @param list Puntero a la lista.
 * @param type Tipo de nodos a incluir en la concatenación.
 * @param hash Hash base para la concatenación.
 * @return Puntero a un nuevo string con el resultado o NULL si falló.
 */
char* string_proc_list_concat(string_proc_list* list, uint8_t type, char* hash) {
    if (list == NULL || hash == NULL) {
        return NULL;
    }
    

    size_t hash_len = strlen(hash);
    char* result = (char*)malloc(hash_len + 1);
    if (result == NULL) {
        return NULL;
    }
    strcpy(result, hash);
    
    string_proc_node* current = list->first;
    while (current != NULL) {
        if (current->type == type && current->hash != NULL) {
            char* temp = str_concat(result, current->hash);
            
            if (temp == NULL) {
                // Si falla la concatenación, devolvemos lo que teníamos hasta ahora
                return result;
            }
            
            free(result);
            result = temp;
        }
        
        current = current->next;
    }
    
    return result;
}

/** AUX FUNCTIONS **/

/**
 * Libera toda la memoria de una lista y sus nodos.
 *
 * @param list Puntero a la lista a destruir.
 */
void string_proc_list_destroy(string_proc_list* list) {
    if (list == NULL) {
        return;
    }

    string_proc_node* current_node = list->first;
    string_proc_node* next_node = NULL;
    
    while (current_node != NULL) {
        next_node = current_node->next;
        string_proc_node_destroy(current_node);
        current_node = next_node;
    }
    
    free(list);
}

/**
 * Libera la memoria de un nodo.
 *
 * @param node Puntero al nodo a destruir.
 */
void string_proc_node_destroy(string_proc_node* node) {
    if (node == NULL) {
        return;
    }
    
    // No liberamos node->hash porque ese puntero es propiedad del caller
    free(node);
}

/**
 * Concatena dos strings a y b.
 *
 * @param a Primer string.
 * @param b Segundo string.
 * @return Puntero a un nuevo string con la concatenación o NULL si falló.
 */
char* str_concat(char* a, char* b) {
    if (a == NULL || b == NULL) {
        return NULL;
    }
    
    size_t len1 = strlen(a);
    size_t len2 = strlen(b);
    size_t total_length = len1 + len2;
    
    char* result = (char*)malloc(total_length + 1);
    if (result == NULL) {
        return NULL;
    }
    
    strcpy(result, a);
    strcat(result, b);
    
    return result;
}

/**
 * Imprime el contenido de la lista en el archivo especificado.
 *
 * @param list Puntero a la lista a imprimir.
 * @param file Archivo donde se escribirá la información.
 */
void string_proc_list_print(string_proc_list* list, FILE* file) {
    if (list == NULL || file == NULL) {
        return;
    }
    
    uint32_t length = 0;
    string_proc_node* current_node = list->first;
    
    // Contamos los nodos
    while (current_node != NULL) {
        length++;
        current_node = current_node->next;
    }
    
    fprintf(file, "List length: %d\n", length);
    
    // Imprimimos cada nodo
    current_node = list->first;
    while (current_node != NULL) {
        fprintf(file, "\tnode hash: %s | type: %d\n", 
                current_node->hash ? current_node->hash : "(null)", 
                current_node->type);
        current_node = current_node->next;
    }
}


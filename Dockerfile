FROM ubuntu:24.04

# Set environment variables to avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Etc/UTC

# Install required dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    make \
    gdb \
    expect \
    grep \
    python3 \
    python3-pip \
    valgrind \
    binutils \
    nasm \
    ltrace \
    strace \
    vim \
    less \
    file \
    && rm -rf /var/lib/apt/lists/*

# Create a directory for the application
WORKDIR /app

# Copy the project files
# Note: The actual copying happens during docker build with the context
COPY . .

# Make scripts e RUNN find . -name "*.sh" -exec chmod +x {} \;

# Build the project
RUN cd ej1 && make clean && make || echo "Build failed, continuing anyway"  
RUN cd ../

# GDB configuration
RUN mkdir -p /root/.config/gdb && \
    echo "set auto-load safe-path /" > /root/.config/gdb/gdbinit && \
    echo "set disassembly-flavor intel" >> /root/.config/gdb/gdbinit && \
    echo "set history save" >> /root/.config/gdb/gdbinit

# Display system information
RUN echo "Architecture: $(uname -m)"
RUN echo "Kernel: $(uname -r)"
RUN echo "Distribution: $(lsb_release -ds)"

# Set the default command to open a shell
CMD ["/bin/bash"]
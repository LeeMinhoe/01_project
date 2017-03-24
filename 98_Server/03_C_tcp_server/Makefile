CC = gcc
CFLAGS = -W 
OBJS = main.o
TARGET = server_exe

$(TARGET) : main.o
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJS)


main.o : main.c
	$(CC) $(CFLAGS) -c -o main.o main.c

clean :
	rm *.o server_exe



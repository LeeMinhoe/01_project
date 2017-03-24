CC = g++
CFLAGS = -W 
OBJS = udp.o tcp.o main.o
TARGET = server_exe

$(TARGET) : udp.o tcp.o main.o
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJS)

udp.o : udp.cc
	$(CC) $(CFLAGS) -c -o udp.o udp.cc

tcp.o : tcp.cc
	$(CC) $(CFLAGS) -c -o tcp.o tcp.cc

main.o : main.cc
	$(CC) $(CFLAGS) -c -o main.o main.cc

clean :
	rm *.o server_exe



#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/types.h>
#include <sys/socket.h>
 
#define BUFSIZE 1024

void error_handling(char *message);



struct DS
{
	/*
	int i;
	float f;
	char str[3];
	
	char c[2];
	
	double h;
	*/
	short s;
	unsigned short us;
	int i;
	unsigned int ui;
	float f;
	double d;
	char str[3];
};
struct D1
{
	char c1[11];
	char c2[9];
	char c3[6];
	char c4[10];
	char c5[7];
	char c6[17];
	int i;
	float f;

};
#pragma pack(push, atin_data_definition, 1)
struct D2
{
	char c1[154];
	int i;
};
#pragma pack(pop, atin_data_definition)
struct D3
{
	char c1[128];
	int i;
};

int main(int argc, char **argv)
{
	int serv_sock;
	int clnt_sock;
	char message[BUFSIZE];
	int str_len;
	int i=1;
 
	struct sockaddr_in serv_addr;
	struct sockaddr_in clnt_addr;
	int clnt_addr_size;
	struct DS ds;
	struct D1 d1;
	struct D2 d2;
	struct D3 d3;
	
	printf("%d\n", sizeof(d2));
	if(argc != 2) {
		printf("Usage : &s <port>\n", argv[0]);
		exit(1);
	}
 
	serv_sock = socket(PF_INET, SOCK_STREAM, 0);   
	if(serv_sock == -1)
		error_handling("socket() error");
 
	memset(&serv_addr, 0, sizeof(serv_addr));
	serv_addr.sin_family = AF_INET;
	serv_addr.sin_addr.s_addr = htonl(INADDR_ANY);
	serv_addr.sin_port = htons(atoi(argv[1]));
 
	if( bind(serv_sock, (struct sockaddr*)&serv_addr, sizeof(serv_addr) )==-1)
		error_handling("bind() error");
 

	 while(1) {
		if(listen(serv_sock, 5) == -1) 
			error_handling("listen() error");
 
		clnt_addr_size = sizeof(clnt_addr);
          
		clnt_sock = accept(serv_sock, (struct sockaddr*)&clnt_addr, &clnt_addr_size);
		if(clnt_sock == -1)
			error_handling("accept() error");
 


		while( (str_len = read(clnt_sock, message, BUFSIZE)) != 0) {
			//write(clnt_sock, message, str_len);
			//write(1, message, str_len);
			//printf("%s %d\n", message, i);
			

			
		}
		
		close(clnt_sock);      
		fflush(stdin);
		//ds = *((struct DS *)&message);
		if (i % 2 == 1)
		{
			d1 = *((struct D1 *)&message);
			printf("\n %s, %s, %s, %s, %s, %s, %d, %f\n", d1.c1, d1.c2, d1.c3, d1.c4, d1.c5, d1.c6, d1.i, d1.f);
		}
		if (i % 2 == 0)
		{
			d2 = *((struct D2 *)&message);
			printf("\n [D2 is] \n %s %d\n", d2.c1, d2.i);
		}

		//printf("\n%d %f %s\n", ds.i, ds.f, ds.str);
		//printf("\n %d, %hd, %d, %o, %f, %lf, %s\n", ds.s, ds.us, ds.i, ds.ui, ds.f, ds.d, ds.str);
		i++;
	 }
	


	return 0;
}
 
void error_handling(char *message)
{
	fputs(message, stderr);
	fputc('\n', stderr);
	exit(1);
}

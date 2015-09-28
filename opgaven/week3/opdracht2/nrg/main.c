//
//  main.c
//  nrg
//
//  Created by Bart Barnard.
//  Copyright (c) 2015 Bart Barnard. All rights reserved.
//

#include <windows.h>
#include <stdio.h>
#include <stdlib.h>
#include <mysql.h>
#include <string.h>
#include <time.h>
#include <stdbool.h>

#include "main.h"


MYSQL *connection;

int main (int argc, const char * argv[]) {
    connection = mysql_init(NULL);
    
    char mysql_server[100];
    char mysql_user[100];
    char mysql_password[100];

    printf("mysql server locatie: ");
    scanf("%99s", mysql_server);
    printf("mysql user: ");
    scanf("%99s", mysql_user);
    printf("mysql password: ");
    scanf("%99s", mysql_password);

    if(connection == NULL) {
        fprintf(stderr, "%s\n", mysql_error(connection));
        exit(1);
    } 

    if(mysql_real_connect(connection, mysql_server, mysql_user, mysql_password, "nrg", 0, 0, 0) == NULL) {
        fprintf(stderr, "%s\n", mysql_error(connection));
        mysql_close(connection);
        exit(1);
    }

    printf("\nConnected to database.\n");
    
    time_t t;
    srand((unsigned int)time(&t));
    
    int aantal;
    int apparaten;
    printf("Aantal huishoudens: ");
    scanf("%d", &aantal);
    printf("Maximaal aantal apparaten per huishouden: ");
    scanf("%d", &apparaten);
    
    create_nrg_database(aantal, apparaten);
    
    mysql_close(connection);
    return 0;
}

void create_nrg_database(int huishoudens, int max_apparaten) {
    // OPGAVE 2.3 VAN WEEK 2
    // Je hoeft er niet per se voor te zorgen dat er maar één exemplaar
    // van een type apparaat aan een huishouden wordt toegekend (het mag
    // uiteraard wel, maar voegt weinig toe aan de algemene functionaliteit
    // of leerdoelen).

    printf("Aanmaken van %d huishoudens\n", huishoudens);

    int i;
    int j;

    for(i = 0; i < huishoudens; i++) {
        int huishouden = create_huishouden();
        printf("huishouden %d aangemaakt\n", huishouden);

        int aantal_apparaten = randomNr(1, max_apparaten, -1);
        printf("%d apparaten toevoegen aan huishouden: %d\n", aantal_apparaten, huishouden);

        for(j = 0; j < aantal_apparaten; j++) {
            int apparaat = apparaat_voor_huishouden(huishouden);
        
            printf("metingen voor apparaat: %d\n", apparaat);
            meting_voor_apparaat(apparaat);
        }
    }

    printf("%d huishoudens aangemaakt\n", huishoudens);

    return;
}

void meting_voor_apparaat(int avh) {
    // We genereren een getal (volgens een pseude-normaal) dat ligt tussen de 250 en de 750
    // voor elk uur van de dag gedurence een maand.
    // trucje, zie: http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.157.4299&rep=rep1&type=pdf
    
    char jaarmaand[12];
    maandAsString(jaarmaand);
    
    struct tm current;
    time_t timenow;
    time(&timenow);
    current = *localtime(&timenow);
    int month = current.tm_mon+1;
    int year = current.tm_year+1900;
    int num_days = numberOfDays(month, year);
    
    for (int dag=1; dag<=num_days; dag++) {
       for (int hrs=0; hrs<24; hrs++) {
           int waarde1 = randomNr(250, 750, -1);
           int waarde2 = randomNr(250, 750, -1);
           int waarde3 = randomNr(250, 750, -1);
           int meting = (int)(waarde1+waarde2+waarde3)/3;
        
           char sql[1024];
           snprintf(sql, sizeof(sql), "insert into meting (app_hh, datum, tijd, waarde) values (%d, '%s-%d', '%d:00', %d)", avh, jaarmaand, dag, hrs, meting);
            mysql_query(connection, sql);
       }
        
    }
}

int apparaat_voor_huishouden(int huishouden) {
    char sql[1024];
    snprintf(sql, sizeof(sql), "insert into apparaat_huishouden (huishouden_fk, apparaat_fk) values (%d, (select id from apparaat order by rand() limit 1))", huishouden);
    mysql_query(connection, sql);
    return (int)mysql_insert_id(connection);
}


int create_huishouden() {
    int huisnummer;
    int grootte;

    mysql_query(connection, "select postcode,minnumber,maxnumber,numbertype from postcode order by rand() limit 1");
    MYSQL_RES *rv = mysql_store_result(connection);
    MYSQL_ROW strtData = mysql_fetch_row(rv);
    
    int min = atoi(strtData[1]);
    int max = atoi(strtData[2]);
    huisnummer = (strcmp(strtData[3],  "even")==0) ? randomNr(min, max, 0) : randomNr(min, max, 1);
    grootte = randomNr(1, 6, -1);
    
    char sql[1024];
    snprintf(sql, sizeof(sql), "insert into huishouden(postcode, huisnummer, grootte) values('%s', %d, %d);", strtData[0], huisnummer, grootte);
    mysql_query(connection, sql);
    mysql_free_result(rv);
    
    return (int)mysql_insert_id(connection);
}



// ******** HELPERS ********** //

void maandAsString(char* buffer) {
    // returning a pointer to a char[] as a means of returning a string.
    // see: http://stackoverflow.com/questions/1496313/returning-c-string-from-a-function for discussion.
    
    struct tm current;
    time_t timenow;
    time(&timenow);
    current = *localtime(&timenow);
    int month = current.tm_mon+1;
    int year = current.tm_year+1900;
    
    snprintf(buffer, 11, "%d-%d", year, month); //magic number, who cares.
}


int numberOfDays(int month, int year) {
    int numberOfDays;
    if (month == 4 || month == 6 || month == 9 || month == 11)
        numberOfDays = 30;
    else if (month == 2) {
        bool isLeapYear = (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
        if (isLeapYear)
            numberOfDays = 29;
        else
            numberOfDays = 28;
    }  
    else  
        numberOfDays = 31;
    
    return numberOfDays;
}



int randomNr(int min, int max, int type) {
    //even: type=0; odd: type=1; other: type=-1
    int output = min + (rand() % (int)(max - min + 1));
    if ( (type==0 && (output%2 != 0)) || (type==1 && (output%2 == 0)) ) {
        output++;
    }
    if (output>max) output -= 2;

    return output;
}

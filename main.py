# encoding: utf-8

def print_calendar():
    #String initializers
    mS = ""
    weekDayCounter = 5 #este año empieza en viernes 1 de enero
    monthCounter = 1
    cD = "Error: Invalid Day"
    cM = "Error: Invalid Month"
    nDias = 0

    for j in range (1, 13):
        if (monthCounter == 1):
            cM = "Enero"
            nDias = 31
        if (monthCounter == 2):
            cM = "Febrero"
            nDias = 28
        if (monthCounter == 3):
            cM = "Marzo"
            nDias = 31
        if (monthCounter == 4):
            cM = "Abril"
            nDias = 30
        if (monthCounter == 5):
            cM = "Mayo"
            nDias = 31
        if (monthCounter == 6):
            cM = "Junio"
            nDias = 30
        if (monthCounter == 7):
            cM = "Julio"
            nDias = 31
        if (monthCounter == 8):
            cM = "Agosto"
            nDias = 31
        if (monthCounter == 9):
            cM = "Setiembre"
            nDias = 30
        if (monthCounter == 10):
            cM = "Octubre"
            nDias = 31
        if (monthCounter == 11):
            cM = "Noviembre"
            nDias = 30
        if (monthCounter == 12):
            cM = "Diciembre"
            nDias = 31

        monthCounter += 1
        if monthCounter >= 13:
            monthCounter = 1

        mS += cM + "\n"

        for i in range(1, nDias+1):
            if (weekDayCounter == 1):
                cD = "Lunes "
            if (weekDayCounter == 2):
                cD = "Martes "
            if (weekDayCounter == 3):
                cD = "Miércoles "
            if (weekDayCounter == 4):
                cD = "Jueves "
            if (weekDayCounter == 5):
                cD = "Viernes "
            if (weekDayCounter == 6):
                cD = "Sabado "
            if (weekDayCounter == 7):
                cD = "Domingo "

            weekDayCounter += 1
            if weekDayCounter >= 8:
                weekDayCounter = 1

            mS += "\t" + cD + str(i) + "\n"





    print(mS)


if __name__ == '__main__':
    print_calendar()


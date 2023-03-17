import sqlite3


def listele():
    baglanti = sqlite3.connect("chinook/chinook.db")
    cursor = baglanti.execute("select FirstName,LastName from Customers")

    for satir in cursor:
        print(satir[0])


    baglanti.close

listele()
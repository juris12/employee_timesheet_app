Task 1. finished in 1.28h

📌 Uzdevums

Izveidot WEB aplikāciju (vēlams izmantot Python):
📍 Sākuma lapa /

    Parāda sarakstu ar visiem darbinieku username
    Iespēja veikt username meklēšanu

📍 Darbinieka skatījums

    Klikšķinot uz kāda darbinieka username, atveras lapa/skats, kur:
        Redzama tabula ar divām kolonnām: date, hours_worked
        Tabulā katrai dienai tiek summētas visas nostrādātās stundas šajā datumā
            📌 Piemērs:
            Ja vienā dienā ir divi ieraksti ar 4h un 3.5h — kopsumma būs 7.5
        Tabula sakārtota pēc date DESC

Izdarītais:

1. Tika izveidota django aplikācija.
aplikacijas admin panelī ir iespējams rediģēt un pievienot darbiniekus un nostrādātās stundas.
2. Tika pievienoti papildus ģenerēti dati. Tos iespējams pievienot /data/create_new_employees
![image](https://github.com/user-attachments/assets/aab6054e-4c07-4be4-93a8-a72a310ed0d3)

4. citas lapas ietver:
/ pārmaršrutē uz /employees

/employees
ir pieejams darbinieku saraksts ar meklēšanas funkcionalitāti. Vienlaicīgi ir iespējams atlasīt 60 vai 120 darbiniekus.
![image](https://github.com/user-attachments/assets/7097f5d7-dec5-414a-8887-6bfc23ade164)

/employees/detail/<id>/
ir redzami visi datumi kuros persona ir strādājusi un nostrādāto stundu skaits dienā un vienkāršī parametri.(desktop platformā ir pieejams grafiks).
![image](https://github.com/user-attachments/assets/f110c29a-1f3d-424d-8bc8-ec636f656305)

/employees/detail/<id>/date/<date>
Ir redzams katrā datuma ieraksti un to summa.
![image](https://github.com/user-attachments/assets/3f84fc16-39b9-4018-ac81-998133540da5)

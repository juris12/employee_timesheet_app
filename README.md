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

4. citas lapas ietver:
/ pārmaršrutē uz /employees

/employees
ir pieejams darbinieku saraksts ar meklēšanas funkcionalitāti. Vienlaicīgi ir iespējams atlasīt 60 vai 120 darbiniekus.

/employees/detail/<id>/
ir redzami visi datumi kuros persona ir strādājusi un nostrādāto stundu skaits dienā un vienkāršī parametri.(desktop platformā ir pieejams grafiks).

/employees/detail/<id>/date/<date>
Ir redzams katrā datuma ieraksti un to summa.
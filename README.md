# server_client_rasp
client.py -aplikacja imitująca terminal wysyłajaca informacje do brokera mqtt ustawionego na loklany adres ip (numery ip w cliencie i serverze muszą być takie same i odpowiadać adresowi ip urządzenia na które wysyłamy wiadomości ).
Żeby przerpowadzić komunikację między dwoma aplikacjami należy na urządzeniu lokalnym do którego chcemy się połaczyć zainstalować brokera mosquitto i włączyć subskrypcje tematu "RFID" (mosquitto_sub -t RFID)
obsługa client.py
podaj jak chcesz nazwać terminal w cudzysłowiu
kolejne użycia karty symuluj przez wpisanie w cudzysłowiu numeru karty

server.py - aplikacja serwerowa równolegle obsługująca zdarzenia oraz prosty iterface tekstowy, żeby poznać jak działa wystarczy wpisać 'help' , wszystko powinno po tym być jasne. Zgłoszenia z niedodanych terminali nie są obsługiwane, zgłoszenia z obsługiwanych terminali z numerem nie przypisanym do pracownika trafiajądo osobnego wspólnego obiektu. Tylko zgłoszenia spełniające dwa powyższe warunki są obsługiwane.

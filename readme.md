<h1>Сервер точного времени</h1>
<p>Сервер точного времени, который «врет» на заданное в своем конфигурационном файле число секунд. Сервер прослушивает 123 порт UDP. Время сервер узнает
либо у ОС, либо у другого надежного сервера точного времени, например, time.windows.com.
В конфигурационном файле сервера указано, на сколько секунд он должен «врать», т. е. из
точного времени сервер вычитает или прибавляет указанное число секунд.
</p>
<p>Клиент, подключившийся к серверу, получает от него точное время, с учетом «вранья» сервера.</p>
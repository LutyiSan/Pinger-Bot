# Pinger-Bot
Программа пингует сетевые устройства из списка подсети раз в час(время можно изменить). В случае отсутствия связи отправляет сообщение в Телеграм-Бот, с указанием: Статус связи ("OK" или "FAIL"),
IP-адрес устройства, его названия и TIMESTAMP.
Так же записывает статус связи в файл data/net_anynumber_ping_state.txt. И дублирует статус FAIL в файл data/net_anynumber_ping_fail.txt. 
Список контролируемых устройств находится в файле data/all_anynumber.txt

# VPN MVP по ТЗ

Состав:
- `backend/` — FastAPI API: `/api/client/auth`, `/api/client/config`, `/api/client/report`, webhook оплаты Telegram.
- `flutter_app/` — Flutter UI: ввод ключа, главный экран, аккаунт, переход в Telegram.
- `infra/` — пример TLS reverse proxy.

## Запуск API
```bash
cd vpn_mvp
docker compose up --build
curl http://localhost:8000/health
curl -X POST http://localhost:8000/admin/seed -H 'x-api-secret: change-me'
```

## Выдача ключа после оплаты
Telegram-бот или платежный обработчик вызывает:
```bash
curl -X POST http://localhost:8000/api/telegram/payment-success \
  -H 'Content-Type: application/json' \
  -H 'x-api-secret: change-me' \
  -d '{"tg_user_id":123,"provider_payment_id":"pay_1","amount":299,"days":30}'
```
В ответ при первом платеже вернется `token`, который пользователь вводит в приложение.

## Запуск Flutter
```bash
cd flutter_app
flutter pub get
flutter run --dart-define=API_BASE=http://10.0.2.2:8000
```
Для iOS/real device укажите публичный HTTPS API.

## Что нужно доделать для production
1. Нативный Android `VpnService` + sing-box/xray-core через MethodChannel.
2. iOS `NetworkExtension PacketTunnelProvider` и entitlement от Apple.
3. Индексированный поиск ключей: HMAC(token) в БД + bcrypt/argon2 для защиты.
4. Админка серверов, мониторинг, реальные health checks и load_score.
5. Webhook конкретного провайдера платежей: YooKassa / CryptoBot / Telegram Stars.
6. No-log настройки VPN nodes и отдельные секреты на каждый сервер.

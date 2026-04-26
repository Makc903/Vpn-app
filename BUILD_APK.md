# Сборка APK

В этой среде нет Flutter SDK / Android SDK, поэтому APK нужно собрать локально или через GitHub Actions.

## Локально

```bash
cd flutter_app
flutter create --platforms=android .
flutter pub get
flutter build apk --debug
```

APK появится здесь:

```text
flutter_app/build/app/outputs/flutter-apk/app-debug.apk
```

## Через GitHub Actions

1. Загрузите проект в GitHub-репозиторий.
2. Откройте вкладку **Actions**.
3. Запустите workflow **Build Android APK**.
4. Скачайте artifact `vpn-mvp-debug-apk`.


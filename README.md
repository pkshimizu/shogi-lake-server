# Shogi Lake Server

## 開発
### コンテナ起動
```shell
docker-compose up
```

[localhost:15000](http://localhost:15000)にアクセスして動作を確認する

### パッケージの追加
```shell
docker-compose run api python -m pip install {package name}
docker-compose run api python -m pip freeze > app/requirements.txt
```

追加したパッケージをコンテナに反映させるためには以下のコマンドを事項して、コンテナを再ビルドする
```shell
docker-compose build
```

### lint, formatter
```shell
docker-compose run api black api
```

### テスト実行
```shell
docker-compose run api pytest
```

### マイグレーション
マイグレーションファイル生成
```shell
docker-compose run api flask db migrate
```
マイグレーション実行
```shell
docker-compose run api flask db upgrade
```
マイグレーションのロールバック
```shell
docker-compose run api flask db downgrade
```

### APIドキュメント
コンテナを起動して、 http://localhost:15000 を開く

## デプロイ
masterブランチにpushすると、dev環境にデプロイされます

本番環境へのデプロイは、T.B.D

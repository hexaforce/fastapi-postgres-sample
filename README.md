# fastapi-postgres-sample

# 環境設定
```bash

poetry env use python3.11

poetry update
```






# テーブルの変更する場合はマイグレーションを発行します

### 1.新規マイグレーションを作成
```bash
# DB起動
make up

# マイグレーション発行
make revision
```

### 2.マッピングモデルの更新

```bash
# model更新
make model
```

# Swagger UI
* http://localhost/v1/docs


# Test
```
make test
```
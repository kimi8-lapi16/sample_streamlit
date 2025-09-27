# sample_streamlit
このリポジトリは、`devcontainer` 上で動作する簡単な Streamlit Web アプリのサンプルです。

## 🧰 セットアップ
- VSCode に以下の拡張機能を入れる  
  - Remote Development
  - Dev Containers

## 立ち上げ手順
  1. VSCodeでこのリポジトリを開いて、`reopen in container`を実行(dockerも立ち上げておく)
  2. devcontainerで開けたら、 ターミナルで`streamlit run app/main.py --server.address=0.0.0.0`を実行
  3. ローカルのアプリが http://localhost:8501/ で起動

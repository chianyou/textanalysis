# 使用 Azure 建立並運行文字分析應用程式

這個 README 文件將引導你建立並在 Azure 上運行一個使用文字分析服務的 Flask 應用程式。這個應用程式能夠進行情感分析並將結果翻譯成繁體中文。

## 步驟

1. **在 Azure 上建立資源群組**

    在 Azure 上建立一個資源群組，名稱為 `textanalysis`。

2. **建立翻譯工具和文字分析**

    在 Azure 上建立兩個服務，分別是翻譯工具和文字分析服務。確保定價層都選擇為 Free F0。

3. **輸入端點和金鑰**

    從 Azure 取得翻譯工具和文字分析服務的端點和金鑰。

4. **構建 Docker 映像檔**

    在本地端運行以下指令，建立 Docker 映像檔：

    ```bash
    docker build -t my-flask-app .
    ```

5. **在本地端運行 Docker 容器**

    在本地端運行以下指令，啟動 Docker 容器：

    ```bash
    docker run -p 8080:8080 my-flask-app
    ```

6. **測試成功後結束**

    測試應用程式是否成功運行，並確保功能正常。

7. **登入 Azure**

    在命令列中使用以下指令登入 Azure：

    ```bash
    az login
    ```

8. **建立 Azure 容器註冊表**

    使用以下指令在 Azure 上建立容器註冊表：

    ```bash
    az acr create --resource-group textanalysis --name finalregistry10317 --sku Basic
    ```

9. **登入 Azure 容器註冊表**

    使用以下指令登入剛剛建立的 Azure 容器註冊表：

    ```bash
    az acr login --name finalregistry10317
    ```

10. **標記 Docker 映像檔**

    使用以下指令標記 Docker 映像檔：

    ```bash
    docker tag my-flask-app finalregistry10317.azurecr.io/my-flask-app:v1
    ```

11. **推送 Docker 映像檔到 Azure 容器註冊表**

    使用以下指令推送 Docker 映像檔到 Azure 容器註冊表：

    ```bash
    docker push finalregistry10317.azurecr.io/my-flask-app:v1
    ```

12. **建立容器執行個體**

    在 Azure 頁面中，找到剛剛建立的容器註冊表，並建立一個容器執行個體。

13. **設定容器執行個體**

    在容器執行個體的設定中，確保新增了 8080 port，以便能夠訪問 Flask 應用程式。

14. **執行**

    完成上述步驟後，你的 Flask 應用程式應該已經在 Azure 上運行。你可以通過瀏覽器訪問該應用程式的 URL，並開始使用文字分析功能。


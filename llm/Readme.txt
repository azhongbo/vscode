
Continue 中的技術細節
1. 程式碼切片 (Chunking)
語言： 主要由 TypeScript 處理。
方式： Continue 運行在 VS Code 內，主要使用 TypeScript 來解析檔案結構。它會使用類似 tree-sitter 的工具（這是一個用 C 寫但有 JS 綁定的解析器），來識別程式碼中的 function、class 等邊界，確保切出來的片段是有意義的，而不是隨機切斷。

2. 向量化 (Embedding)
語言： 涉及 C++/Python/Rust (模型層) 與 JavaScript (呼叫層)。
方式： * 如果你用 OpenAI 的 Embedding，JavaScript 只是負責發送 API 請求。
如果你在本地運行（例如透過 Ollama 或 Transformers.js），背後跑的是高度優化的矩陣運算程式庫（如 llama.cpp）。雖然現在有 ONNX 或 WebAssembly 讓 JS 也能跑模型，但效能最強的還是 C++/Rust。

3. 建立向量資料庫 (Vector Database)
語言： Rust (核心) + JavaScript (接口)。
工具： Continue 預設使用 LanceDB。
LanceDB 的核心是用 Rust 寫的，因為處理大量向量的儲存與檢索需要極高的記憶體效率和速度。
JavaScript 只是作為「客戶端」去把資料存進去或撈出來。

4. 相似度檢索 (Similarity Search)
語言： Rust (數學計算)。
原理： 檢索的核心是餘弦相似度 (Cosine Similarity) 的數學運算。
這涉及大量的向量點積運算。為了追求毫秒級的反應速度，這部分邏輯通常在向量資料庫的 Rust 層級就處理掉了，JS 只是接收最後的排名結果。
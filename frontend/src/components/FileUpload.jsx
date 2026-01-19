import { useState } from "react";
import { analyzeChat } from "../services/api";

const FileUpload = ({ onResult }) => {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    if (!file) return alert("Please upload a chat file");

    setLoading(true);
    try {
      const response = await analyzeChat(file);
      onResult(response.data);
    } catch (err) {
      alert("Error analyzing chat");
    } finally {
      setLoading(false);
    }
  };

  return (
   <div className="upload-card">
  <h2>📤 Upload WhatsApp Chat</h2>
  <div className="upload-row">
    <input
      type="file"
      accept=".txt"
      onChange={(e) => setFile(e.target.files[0])}
    />
    <button onClick={handleSubmit} disabled={loading}>
      {loading ? "Analyzing..." : "Analyze"}
    </button>
  </div>
</div>

  );
};

export default FileUpload;

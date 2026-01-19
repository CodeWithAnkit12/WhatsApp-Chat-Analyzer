import { useState } from "react";
import FileUpload from "./components/FileUpload";
import ActivityChart from "./components/ActivityChart";
import ActiveUsers from "./components/ActiveUsers";
import "./styles/app.css";

function App() {
  const [result, setResult] = useState(null);

  return (
    <div className="page">
      <div className="container">
        <header className="header">
          <h1>📱 WhatsApp Chat Analyzer</h1>
          <p>Analyze group activity & engagement in seconds</p>
        </header>

        <FileUpload onResult={setResult} />

        {result && (
          <div className="results">
            <ActivityChart data={result.last_7_days_stats} />
            <ActiveUsers users={result.active_4_days_users} />
          </div>
        )}
      </div>
    </div>
  );
}

export default App;

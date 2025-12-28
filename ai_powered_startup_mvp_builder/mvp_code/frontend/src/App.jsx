import React, { useState } from 'react';
import { History, Loader2, Sparkles } from 'lucide-react';
import ReactMarkdown from 'react-markdown';

function App() {
  const [url, setUrl] = useState('');
  const [tone, setTone] = useState('Professional Mentor');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const handleRefine = async () => {
    if (!url) return alert("Please enter a URL");
    
    setLoading(true);
    setResult(null);

    try {
      const response = await fetch('http://localhost:8000/refine', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url, tone }),
      });
      
      const data = await response.json();
      setResult(data.refined_content);
    } catch (error) {
      console.error("Error:", error);
      setResult("An error occurred while connecting to the server.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-slate-50 flex flex-col items-center py-12 px-4">
      
      {/* Header */}
      <div className="w-full max-w-2xl flex justify-between items-center mb-8">
        <h1 className="text-3xl font-bold text-blue-600 flex items-center gap-2">
          AI Content Refiner
        </h1>
        <button className="text-slate-400 hover:text-blue-600 transition">
          <History size={24} />
        </button>
      </div>

      {/* Main Card */}
      <div className="w-full max-w-2xl bg-white rounded-xl shadow-lg border border-slate-100 p-8 min-h-[400px] flex flex-col justify-center">
        
        {loading ? (
          // Loading State
          <div className="flex flex-col items-center justify-center space-y-4 animate-in fade-in duration-300">
            <Loader2 size={64} className="text-blue-500 animate-spin" />
            <p className="text-lg text-slate-500 font-medium">Processing your content...</p>
          </div>
        ) : result ? (
          // Result State
          <div className="animate-in fade-in slide-in-from-bottom-4 duration-500">
            <div className="flex justify-between items-center mb-4 border-b pb-2">
              <h2 className="text-lg font-semibold text-slate-700">Refined Content ({tone})</h2>
              <button 
                onClick={() => setResult(null)}
                className="text-sm text-blue-500 hover:underline"
              >
                Refine Another
              </button>
            </div>
            <div className="prose prose-slate max-w-none text-slate-600">
              <ReactMarkdown>{result}</ReactMarkdown>
            </div>
          </div>
        ) : (
          // Input State
          <div className="flex flex-col space-y-6 animate-in fade-in duration-300">
            
            {/* URL Input */}
            <div className="flex gap-2">
              <input
                type="text"
                placeholder="Paste documentation URL here..."
                value={url}
                onChange={(e) => setUrl(e.target.value)}
                className="flex-1 p-3 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition"
              />
              <button 
                className="bg-blue-600 text-white px-6 py-3 rounded-lg font-medium hover:bg-blue-700 transition"
                onClick={() => navigator.clipboard.readText().then(text => setUrl(text))}
              >
                Paste
              </button>
            </div>

            {/* Tone Selector */}
            <div className="space-y-2">
              <label className="block text-sm font-medium text-slate-700">Select Tone:</label>
              <select 
                value={tone}
                onChange={(e) => setTone(e.target.value)}
                className="w-full p-3 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white"
              >
                <option>Professional Mentor</option>
                <option>Casual Developer</option>
                <option>Enthusiastic</option>
              </select>
            </div>

            {/* CTA Button */}
            <button 
              onClick={handleRefine}
              className="w-full bg-blue-600 text-white p-4 rounded-lg font-bold text-lg hover:bg-blue-700 transition shadow-md hover:shadow-lg flex justify-center items-center gap-2"
            >
              <Sparkles size={20} />
              Generate Content
            </button>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;

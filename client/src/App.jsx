import { useState } from "react";
import InputForm from "./components/InputForm";
import ResultCard from "./components/ResultCard";

function App() {
    const [result, setResult] = useState("");

    const labelMap = {
        "You're Fine": "Chill, you good",
        "Mild Overthinking": "Godd, stop think too much",
        "Seek Emotional Support": "Drop the phone and go for a walk or something",
    };


    const handleSubmit = async (text) => {
        try {
            const res = await fetch("http://127.0.0.1:5000/predict", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ text }),
            });

            const data = await res.json();
            setResult(labelMap[data.category] || "Unrecognized mood");

        } catch (err) {
            console.error("Error:", err);
            setResult("Something went wrong. Try again.");
        }
    };

    return (
        <div className="min-h-screen flex flex-col items-center justify-center p-8">
            <h1 style={{ color: "#F787ED" }} className="mb-4">WorryPal</h1>
            <InputForm onSubmit={handleSubmit} />
            <ResultCard result={result} />
        </div>
    );
}

export default App;

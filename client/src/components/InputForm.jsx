import { useState } from "react";

const InputForm = ({ onSubmit }) => {
    const [text, setText] = useState("");

    const handleSubmit = (e) => {
    e.preventDefault();
    if (!text.trim()) return;
    onSubmit(text);
    setText("");
    };

    return (
    <form onSubmit={handleSubmit} className="flex flex-col items-center gap-4">
        <textarea
        placeholder="What’s on your mind?"
        className="w-full p-4 rounded-xl shadow-md border"
        rows={4}
        value={text}
        onChange={(e) => setText(e.target.value)}
        />
        <button
        type="submit"
        className="bg-black text-white px-6 py-2 rounded-xl shadow hover:opacity-90">
        HELP
        </button>
    </form>
    );
};

export default InputForm;

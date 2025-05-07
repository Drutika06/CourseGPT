import express from "express";
import cors from "cors";
import dotenv from "dotenv";
import OpenAI from "openai";

dotenv.config();

const app = express();
const PORT = process.env.PORT || 5000;

app.use(cors());
app.use(express.json());

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

app.get("/", (req, res) => {
  res.json({ message: "Server is running..." });
});

app.post("/api/generate-lesson", async (req, res) => {
  const { topic } = req.body;

  if (!topic) {
    return res.status(400).json({ error: "Topic is required" });
  }

  try {
    const completion = await openai.chat.completions.create({
      model: "gpt-4",
      messages: [
        { role: "system", content: "You are an expert educational content creator." },
        { role: "user", content: `Create a structured lesson plan on: ${topic}` }
      ],
    });

    const content = completion.choices[0].message.content;
    res.json({ lesson: content });
  } catch (error) {
    console.error("Error generating lesson:", error);
    res.status(500).json({ error: "Failed to generate lesson" });
  }
});

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});

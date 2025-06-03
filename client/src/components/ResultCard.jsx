// ResultCard.jsx
import { motion } from "framer-motion";

const ResultCard = ({ result }) => {
    if (!result) return null;

    return (
        <motion.div
            className="text-xl text-center mt-6"
            initial={{ y: -20, opacity: 0 }}
            animate={{
                y: [0, -10, 0],
                opacity: 1
            }}
            transition={{
                duration: 2,
                repeat: Infinity,
                ease: "easeInOut"
            }}
        >
            {result}
        </motion.div>

    );
};

export default ResultCard;

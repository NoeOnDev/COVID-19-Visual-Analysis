import express from 'express';
import cors from 'cors';
import { sequelize } from '../database/db.config.js';

export async function server(){
    try {
        await sequelize.authenticate();
        await sequelize.sync();

        const PORT = process.env.PORT || 3000;
        const app = express();
    
        app.use(cors());
        app.use(express.json());
        app.listen(PORT);
    } catch (error) {
        console.error(`Failed to start server: ${error}`);
    }
}
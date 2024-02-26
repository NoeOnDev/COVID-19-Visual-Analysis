import express from 'express';
import morgan from 'morgan';
import cors from 'cors';
import { sequelize } from '../database/db.config.js';
import '../model/association.model.js';

export async function server(){
    try {
        await sequelize.authenticate();
        await sequelize.sync();

        const PORT = process.env.PORT || 3000;
        const app = express();
    
        app.use(cors());
        app.use(express.json());
        app.use(morgan('dev'));
        app.listen(PORT);
    } catch (error) {
        console.error(`Failed to start server: ${error}`);
    }
}
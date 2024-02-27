import { Router } from 'express';
import userRoutes from './user.routes.js';

const indexRouter = Router();

indexRouter.use('/user', userRoutes);

export default indexRouter;
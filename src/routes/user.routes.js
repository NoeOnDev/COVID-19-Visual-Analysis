import { Router } from 'express';
import { UserController } from '../controller/user.controller.js';

const router = Router();

router.post('/register', UserController.registerUser);
router.get('/verify/:token', UserController.verifyUser);

export default router;
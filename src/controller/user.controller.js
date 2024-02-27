import { UserService } from '../service/user.service.js';

export class UserController {
    static async registerUser(req, res) {
        try {
            const user = await UserService.registerUser(req.body);
            res.status(201).json(user);
        } catch (error) {
            res.status(400).json({ error: error.message });
        }
    }

    static async verifyUser(req, res) {
        try {
            const user = await UserService.verifyUser(req.params.token);
            res.status(200).json(user);
        } catch (error) {
            res.status(400).json({ error: error.message });
        }
    }
}
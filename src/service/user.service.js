import bcrypt from 'bcryptjs';
import jwt from 'jsonwebtoken';
import { User } from '../model/user.model.js';
import { Token } from '../model/token.model.js';

export class UserService {
    static async registerUser(userData) {
        const user = await User.create(userData);
        return user;
    }
}
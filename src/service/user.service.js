import { v4 as uuidv4 } from 'uuid';
import { User } from '../model/user.model.js';
import { Token } from '../model/token.model.js';
import transporter from '../transporter/mailer.transporter.js';

export class UserService {
    static async registerUser(userData) {
        const user = await User.create(userData);
        const verificationToken = uuidv4();

        const expirationDate = new Date();
        expirationDate.setHours(expirationDate.getHours() + 1);

        await Token.create({ userId: user.id, token: verificationToken, expiresAt: expirationDate });

        await transporter.sendMail({
            from: 'noeon@gmail.com',
            to: user.email,
            subject: 'Account Verification',
            html: `Click <a href="http://localhost:9020/user/verify/${verificationToken}">here</a> to verify your account.`,
        });

        return user;
    }

    static async verifyUser(token) {
        const verificationToken = await Token.findOne({ where: { token } });

        if (!verificationToken) {
            throw new Error('Invalid token');
        }

        const now = new Date();

        if (verificationToken.expiresAt < now) {
            throw new Error('Token expired');
        }

        const user = await User.update({ verified: true }, { where: { id: verificationToken.userId } });

        await Token.destroy({ where: { id: verificationToken.id } });

        return user;
    }
}
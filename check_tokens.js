const { MongoClient } = require('mongodb');

async function checkTokens() {
    const uri = process.env.MONGODB_URI;
    if (!uri) {
        console.log("No MONGODB_URI found. Trying hardcoded if possible or reading from .env.local");
        require('dotenv').config({ path: '.env.local' });
    }
    const client = new MongoClient(process.env.MONGODB_URI);
    try {
        await client.connect();
        const db = client.db('prettyfresh');
        const users = await db.collection('users').find({ deviceTokens: { $exists: true, $not: {$size: 0} } }).toArray();
        console.log(`Found ${users.length} users with tokens:`);
        for (const user of users) {
            console.log(`Email: ${user.email}, Tokens: ${user.deviceTokens.length}`);
        }
    } finally {
        await client.close();
    }
}
checkTokens().catch(console.error);

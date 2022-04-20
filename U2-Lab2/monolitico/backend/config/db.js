import mongoose from 'mongoose';
import colors from 'colors';

const connectDB = async() =>{
    process.env['NODE_ENV'] = "production"  
    process.env['URL_DB_CONNECTION'] = 'mongodb://localhost/bookstore-production'
    try{
        const conn = await mongoose.connect(process.env.URL_DB_CONNECTION,{
            useUnifiedTopology: true,
            useNewUrlParser: true,
            useCreateIndex: true
        })
        
        console.log(`MongoDB is connected:${conn.connection.host}`.yellow)
        console.log('MongoDB_URL=', process.env.URL_DB_CONNECTION)
    }catch(error){
        console.log(`Error to conect to MongoDB: ${error.message}`.red.bold)
        process.exit(1)
    }
}

export default connectDB
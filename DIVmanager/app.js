const express = require("express");
const path =require("path");

const app = express();

app.get("/",(req, res) => {
    //res.send("si sirve");
    res.sendFile(path.join(__dirname + "/index.html"));
});

app.listen(3000,() =>{
    console.long("si sirve",3000);
});
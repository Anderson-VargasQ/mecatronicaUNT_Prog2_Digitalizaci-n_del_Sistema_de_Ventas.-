/* jshint esversion:6 */
const express = require('express');
const ejs = require('ejs');
const mongoose = require('mongoose');
const port = process.env.PORT|| 8080;
const app = express();

/////////configuraciones////////
app.set('view engine', 'ejs');
app.use(express.static('public'));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

/////////CONEXION DB///////////
mongoose.connect('mongodb+srv://grupo_hailpy:1a2b3c4d5e@proyectox.todpx.mongodb.net/test?retryWrites=true&w=majority', {
  useNewUrlParser: true,
  useUnifiedTopology: true
});

///////////////MODELOS////////////////////////////////////////

const ProductoSchema = new mongoose.Schema({
  _id: String,
  categoria: String,
  name: String,
  precio_costo:String,
  precio_venta:String,
  utilidad:String,
  stock:Number,
  reserva:Number,
  stock_disp:Number,

  });
const Base = mongoose.model('Base', ProductoSchema);



///////////////////ROUTES////////////////////
app.get('/', (req, res)=>{
  Base.find((err, pd) =>{
    if (err) {
      console.log(err);
    } else {
      res.render('index', {pr: pd});
    }
  });
});



app.get('/papelh', (req, res)=>{
  Base.find((err, pd) =>{
    if (err) {
      console.log(err);
    } else {
      res.render('papelh', {pr: pd});
    }
  });
});

app.get('/abarrotes', (req, res)=>{
  Base.find((err, pd) =>{
    if (err) {
      console.log(err);
    } else {
      res.render('abarrotes', {pr: pd});
    }
  });
});

app.get('/aceites', (req, res)=>{
  Base.find((err, pd) =>{
    if (err) {
      console.log(err);
    } else {
      res.render('aceites', {pr: pd});
    }
  });
});

app.get('/cafes', (req, res)=>{
  Base.find((err, pd) =>{
    if (err) {
      console.log(err);
    } else {
      res.render('cafes', {pr: pd});
    }
  });
});

app.get('/conservas', (req, res)=>{
  Base.find((err, pd) =>{
    if (err) {
      console.log(err);
    } else {
      res.render('conservas', {pr: pd});
    }
  });
});

app.get('/detergentes', (req, res)=>{
  Base.find((err, pd) =>{
    if (err) {
      console.log(err);
    } else {
      res.render('conservas', {pr: pd});
    }
  });
});

app.get('/galletas', (req, res)=>{
  Base.find((err, pd) =>{
    if (err) {
      console.log(err);
    } else {
      res.render('galletas', {pr: pd});
    }
  });
});

app.get('/leches', (req, res)=>{
  Base.find((err, pd) =>{
    if (err) {
      console.log(err);
    } else {
      res.render('leches', {pr: pd});
    }
  });
});
app.get('/pastas', (req, res)=>{
  Base.find((err, pd) =>{
    if (err) {
      console.log(err);
    } else {
      res.render('pastas', {pr: pd});
    }
  });
});

app.get('/shanpoos', (req, res)=>{
  Base.find((err, pd) =>{
    if (err) {
      console.log(err);
    } else {
      res.render('shanpoos', {pr: pd});
    }
  });
});
/////////////////////////////APP GET//////////////////////////////////////
app.get('/', (req,res)=>{
  res.render('index');
});

app.get('/', (req,res)=>{
  res.render('index');
});

app.get('/abarrotes', (req,res)=>{
  res.render('abarrotes');
});

app.get('/aceites', (req,res)=>{
  res.render('aceites');
});

app.get('/cafes', (req,res)=>{
  res.render('cafes');
});

app.get('/conservas', (req,res)=>{
  res.render('conservas');
});

app.get('/detergentes', (req,res)=>{
  res.render('detergentes');
});

app.get('/galletas', (req,res)=>{
  res.render('galletas');
});

app.get('/leches', (req,res)=>{
  res.render('leches');
});

app.get('/pastas', (req,res)=>{
  res.render('pastas');
});

app.get('/shanpoos', (req,res)=>{
  res.render('shanpoos');
});

app.get('/contactanos', (req, res)=>{
  res.render('contactanos');
});

app.get('/catalogo', (req, res)=>{
  res.render('catalogo');
});

app.get('/aboutus', (req, res)=>{
  res.render('aboutus');
});

app.get('/anuevos_prods', (req, res)=>{
  res.render('anuevos_prods');
});

app.get('/prueba', (req, res)=>{
  res.render('prueba');
});

app.get('/papelh', (req, res)=>{
  res.render('papelh');
});

app.get('/funcreservar', (req, res)=>{
  res.render('funcreservar');
});

app.get('/pagregis', (req, res)=>{
  res.render('pagregis');
});
app.get('/nuevop', (req, res)=>{
  res.render('nuevop');
});

////////////////////////////////////////////////////////////////////////////////////////////

app.post('/nuevop', (req, res)=>{
  const nuevoProducto = new Base({
    _id: req.body._id,
    categoria: req.body.categoria,
    name: req.body.name,
    precio_costo:req.body.precio_costo,
    precio_venta:req.body.precio_venta,
    utilidad:req.body.utilidad,
    stock:req.body.stock,
    reserva:req.body.reserva,
    stock_disp:req.body.stock_disp
  });
  nuevoProducto.save();
  res.redirect('/');
});

//////////////////API REST//////////////////////
app.get('/api/pd', (req, res) => {
  Base.find((err, pd) => {
    if (err) {
      console.log(err);
    } else {
      res.send(pd);
    }
  });
});

app.get('/api/pd/:Producto', (req, res) => {
  Base.findOne({name:req.params.Producto},(err, Producto) => {
    if (err) {
      console.log(err);
    } else {
      res.send(Producto);
    }
  });
});


app.post('/api/pd', (req, res) => {

  const nuevoProducto = new Base({
    _id: req.body._id,
    categoria: req.body.categoria,
    name: req.body.name,
    precio_costo:req.body.precio_costo,
    precio_venta:req.body.precio_venta,
    utilidad:req.body.utilidad,
    stock:req.body.stock,
    reserva:req.body.reserva,
    stock_disp:req.body.stock_disp
  });
  nuevoProducto.save();

  res.send('Producto guardado');
});



////////////////SERVIDOR/////////////////////
app.listen(port, () => {
  console.log(`Servidor en puerto ${port}`);
});


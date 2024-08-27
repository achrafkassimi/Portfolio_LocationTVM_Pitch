import logo from './logo.svg';
import './App.css';
/* import { Home } from './Compenents/home'; 
import { About } from './Compenents/about';
import { Shope } from './Compenents/shope';
import { Contact } from './Compenents/Contact'; */
/* import Prson from './Compenents/card';
import Todolist from './Compenents/arry'; */
import Navbar from './Compenents/Navbar/Navbar'
import Footer from './Compenents/Footer/footer'
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Blog from './pages/Blog';
import Tarif from './pages/Tarif';
import Home from './pages/Home';
import Contact from './pages/Contact';
import Offer from './pages/Offer';
function App() {
  
  return (
    <div>
    <BrowserRouter>
    <Navbar/>
    <Routes>
      <Route path="/" element={<Home/>}/>
      <Route path="/blog" element={<Blog/>}/>
      <Route path="/offer" element={<Offer/>}/>
      <Route path="/contact" element={<Contact/>}/>
      <Route path="/tarif" element={<Tarif/>}/>
    </Routes>
    <Footer/>
    </BrowserRouter>
    
  </div>
  );
}

export default App;

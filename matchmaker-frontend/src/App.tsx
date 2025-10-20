import { useState } from 'react'
import './App.css'
import { Route, Routes, BrowserRouter } from 'react-router-dom'
import { HomePage } from './pages/HomePage.tsx'
import { LoginPage } from './pages/LoginPage.tsx'
import { RegisterPage } from './pages/RegisterPage.tsx'
import { GroupsPage } from './pages/GroupsPage.tsx'
import { Navbar2 } from './components/Navbar2.tsx'

function App() {

  return (
    <>
      <div className="container m-auto">
        <BrowserRouter>
          <Navbar2 />
          <Routes>
            <Route
              path="/"
              element={<HomePage />}
            ></Route>
            <Route
              path="/login"
              element={<LoginPage />}
            ></Route>
            <Route
              path="/register"
              element={<RegisterPage />}
            ></Route>
            <Route
              path="/groups"
              element={<GroupsPage />}
            ></Route>
          </Routes>
        </BrowserRouter>
      </div>
    </>
  )
}

export default App

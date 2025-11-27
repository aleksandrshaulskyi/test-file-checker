import { BrowserRouter, Route, Routes } from 'react-router-dom'

import { Index } from '../pages/index'
import { Login } from '../pages/login/login'
import { Register } from '../pages/register/register'


function App() {
	return (
		<BrowserRouter>
			<Routes>
				<Route path='/register' element={<Register />} />
				<Route path='/login' element={<Login />} />
				<Route path='/' element={<Index />} />
			</Routes>
		</BrowserRouter>
	)
}

export default App

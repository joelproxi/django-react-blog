import React from 'react';
import ReactDOM from 'react-dom/client';

import {RouterProvider, createBrowserRouter} from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.css';

import Root from './routes/Root.tsx';
import ErrorPage from './ErrorPage.tsx';
import PostDetailPage from './pages/PostDetailPage.tsx';
import {postLoader as postListLoader} from './api/loaders.ts';

const router = createBrowserRouter([
  {
    path: '/',
    element: <Root />,
    errorElement: <ErrorPage />,
    loader: postListLoader,
    children: [{path: 'post/:postID', element: <PostDetailPage />}]
  }
]);

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);

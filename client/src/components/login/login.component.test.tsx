import React from 'react';
import { render, screen } from '@testing-library/react';
import Login from './login.component';

describe('Login component', () => {
    it('renders login form', () => {
        render(<Login />);

        expect(screen.getByLabelText("Username:")).toBeInTheDocument();
        expect(screen.getByLabelText("Password:")).toBeInTheDocument();
        expect(screen.getByRole('button', {name: "Submit"})).toBeInTheDocument();
    });
});

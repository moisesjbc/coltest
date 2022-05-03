import React from 'react';
import { render, screen } from '@testing-library/react';
import LoginComponent from './login.component';

describe('Login component', () => {
    it('renders dummy message', () => {
        render(<LoginComponent />);
        expect(screen.getByText('TODO - Fill me')).toBeInTheDocument();
    });
});

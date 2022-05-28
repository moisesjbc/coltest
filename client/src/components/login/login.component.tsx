import React from 'react';

const Login = (): JSX.Element => {
    return (
        <form>
            <label>
                Username:
                <input name="username" type="text" />
            </label>

            <label>
                Password:
                <input name="password" type="password" />
            </label>

            <button type="submit">Submit</button>
        </form>
    );
}

export default Login;
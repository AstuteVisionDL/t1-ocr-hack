import Login from '../routes/auth/Login';
import Register from '../routes/auth/Register';

import loginInstanceName from '../routes/auth/Login/instanceName';
import registerInstanceName from '../routes/auth/Register/instanceName';

const routesConfig = {
  '/': Login,
  [loginInstanceName]: Login,
  [registerInstanceName]: Register,
};

export default routesConfig;
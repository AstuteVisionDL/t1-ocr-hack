import Login from '../routes/auth/Login';
import Register from '../routes/auth/Register';
import Document from '../routes/document';

import loginInstanceName from '../routes/auth/Login/instanceName';
import registerInstanceName from '../routes/auth/Register/instanceName';
import documentInstanceName from '../routes/document/instanceName';

const routesConfig = {
  '/': Document,
  [loginInstanceName]: Login,
  [registerInstanceName]: Register,
  [documentInstanceName]: Document
};

export default routesConfig;
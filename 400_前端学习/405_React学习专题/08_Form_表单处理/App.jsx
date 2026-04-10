import React, { useState } from 'react';

// 1. 基本表单处理示例
function BasicForm() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Submitted:', { name, email });
  };

  return (
    <div style={{ border: '1px solid #dee2e6', padding: '16px', margin: '16px 0' }}>
      <h3>Basic Form</h3>
      <form onSubmit={handleSubmit}>
        <div style={{ margin: '8px 0' }}>
          <label style={{ display: 'block', marginBottom: '4px' }}>Name:</label>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            style={{ padding: '8px', width: '300px' }}
          />
        </div>
        <div style={{ margin: '8px 0' }}>
          <label style={{ display: 'block', marginBottom: '4px' }}>Email:</label>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            style={{ padding: '8px', width: '300px' }}
          />
        </div>
        <button type="submit" style={{ padding: '8px 16px', marginTop: '8px' }}>
          Submit
        </button>
      </form>
    </div>
  );
}

// 2. 表单验证示例
function FormWithValidation() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [errors, setErrors] = useState({});
  const [isSubmitting, setIsSubmitting] = useState(false);

  const validate = () => {
    const newErrors = {};
    if (!name) newErrors.name = 'Name is required';
    if (!email) {
      newErrors.email = 'Email is required';
    } else if (!/\S+@\S+\.\S+/.test(email)) {
      newErrors.email = 'Email is invalid';
    }
    if (!password) {
      newErrors.password = 'Password is required';
    } else if (password.length < 6) {
      newErrors.password = 'Password must be at least 6 characters';
    }
    return newErrors;
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const newErrors = validate();
    if (Object.keys(newErrors).length === 0) {
      setIsSubmitting(true);
      // 模拟 API 调用
      setTimeout(() => {
        console.log('Submitted:', { name, email, password });
        setIsSubmitting(false);
        setName('');
        setEmail('');
        setPassword('');
      }, 1000);
    } else {
      setErrors(newErrors);
    }
  };

  return (
    <div style={{ border: '1px solid #dee2e6', padding: '16px', margin: '16px 0' }}>
      <h3>Form with Validation</h3>
      <form onSubmit={handleSubmit}>
        <div style={{ margin: '8px 0' }}>
          <label style={{ display: 'block', marginBottom: '4px' }}>Name:</label>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            style={{ padding: '8px', width: '300px' }}
          />
          {errors.name && <p style={{ color: 'red', margin: '4px 0 0 0' }}>{errors.name}</p>}
        </div>
        <div style={{ margin: '8px 0' }}>
          <label style={{ display: 'block', marginBottom: '4px' }}>Email:</label>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            style={{ padding: '8px', width: '300px' }}
          />
          {errors.email && <p style={{ color: 'red', margin: '4px 0 0 0' }}>{errors.email}</p>}
        </div>
        <div style={{ margin: '8px 0' }}>
          <label style={{ display: 'block', marginBottom: '4px' }}>Password:</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            style={{ padding: '8px', width: '300px' }}
          />
          {errors.password && <p style={{ color: 'red', margin: '4px 0 0 0' }}>{errors.password}</p>}
        </div>
        <button 
          type="submit" 
          style={{ padding: '8px 16px', marginTop: '8px' }}
          disabled={isSubmitting}
        >
          {isSubmitting ? 'Submitting...' : 'Submit'}
        </button>
      </form>
    </div>
  );
}

// 3. 复杂表单处理示例
function ComplexForm() {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    address: {
      street: '',
      city: '',
      country: ''
    },
    interests: []
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    if (name.includes('.')) {
      const [parent, child] = name.split('.');
      setFormData(prev => ({
        ...prev,
        [parent]: {
          ...prev[parent],
          [child]: value
        }
      }));
    } else {
      setFormData(prev => ({
        ...prev,
        [name]: value
      }));
    }
  };

  const handleCheckboxChange = (e) => {
    const { value, checked } = e.target;
    setFormData(prev => {
      if (checked) {
        return {
          ...prev,
          interests: [...prev.interests, value]
        };
      } else {
        return {
          ...prev,
          interests: prev.interests.filter(item => item !== value)
        };
      }
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Submitted:', formData);
  };

  return (
    <div style={{ border: '1px solid #dee2e6', padding: '16px', margin: '16px 0' }}>
      <h3>Complex Form</h3>
      <form onSubmit={handleSubmit}>
        <div style={{ margin: '8px 0' }}>
          <label style={{ display: 'block', marginBottom: '4px' }}>Name:</label>
          <input
            type="text"
            name="name"
            value={formData.name}
            onChange={handleChange}
            style={{ padding: '8px', width: '300px' }}
          />
        </div>
        <div style={{ margin: '8px 0' }}>
          <label style={{ display: 'block', marginBottom: '4px' }}>Email:</label>
          <input
            type="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            style={{ padding: '8px', width: '300px' }}
          />
        </div>
        <div style={{ margin: '16px 0' }}>
          <h4>Address</h4>
          <div style={{ margin: '8px 0' }}>
            <label style={{ display: 'block', marginBottom: '4px' }}>Street:</label>
            <input
              type="text"
              name="address.street"
              value={formData.address.street}
              onChange={handleChange}
              style={{ padding: '8px', width: '300px' }}
            />
          </div>
          <div style={{ margin: '8px 0' }}>
            <label style={{ display: 'block', marginBottom: '4px' }}>City:</label>
            <input
              type="text"
              name="address.city"
              value={formData.address.city}
              onChange={handleChange}
              style={{ padding: '8px', width: '300px' }}
            />
          </div>
          <div style={{ margin: '8px 0' }}>
            <label style={{ display: 'block', marginBottom: '4px' }}>Country:</label>
            <input
              type="text"
              name="address.country"
              value={formData.address.country}
              onChange={handleChange}
              style={{ padding: '8px', width: '300px' }}
            />
          </div>
        </div>
        <div style={{ margin: '16px 0' }}>
          <h4>Interests</h4>
          <div style={{ margin: '8px 0' }}>
            <input
              type="checkbox"
              id="interest1"
              value="programming"
              checked={formData.interests.includes('programming')}
              onChange={handleCheckboxChange}
            />
            <label htmlFor="interest1" style={{ marginLeft: '8px' }}>Programming</label>
          </div>
          <div style={{ margin: '8px 0' }}>
            <input
              type="checkbox"
              id="interest2"
              value="reading"
              checked={formData.interests.includes('reading')}
              onChange={handleCheckboxChange}
            />
            <label htmlFor="interest2" style={{ marginLeft: '8px' }}>Reading</label>
          </div>
          <div style={{ margin: '8px 0' }}>
            <input
              type="checkbox"
              id="interest3"
              value="sports"
              checked={formData.interests.includes('sports')}
              onChange={handleCheckboxChange}
            />
            <label htmlFor="interest3" style={{ marginLeft: '8px' }}>Sports</label>
          </div>
        </div>
        <button type="submit" style={{ padding: '8px 16px', marginTop: '8px' }}>
          Submit
        </button>
      </form>
    </div>
  );
}

// 4. 实时验证示例
function RealTimeValidationForm() {
  const [formData, setFormData] = useState({
    name: '',
    email: ''
  });
  const [errors, setErrors] = useState({});

  const validate = () => {
    const newErrors = {};
    if (!formData.name) newErrors.name = 'Name is required';
    if (!formData.email) {
      newErrors.email = 'Email is required';
    } else if (!/\S+@\S+\.\S+/.test(formData.email)) {
      newErrors.email = 'Email is invalid';
    }
    return newErrors;
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
    // 实时验证
    setErrors(validate());
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const newErrors = validate();
    if (Object.keys(newErrors).length === 0) {
      console.log('Submitted:', formData);
    } else {
      setErrors(newErrors);
    }
  };

  return (
    <div style={{ border: '1px solid #dee2e6', padding: '16px', margin: '16px 0' }}>
      <h3>Real-time Validation Form</h3>
      <form onSubmit={handleSubmit}>
        <div style={{ margin: '8px 0' }}>
          <label style={{ display: 'block', marginBottom: '4px' }}>Name:</label>
          <input
            type="text"
            name="name"
            value={formData.name}
            onChange={handleChange}
            style={{ padding: '8px', width: '300px' }}
          />
          {errors.name && <p style={{ color: 'red', margin: '4px 0 0 0' }}>{errors.name}</p>}
        </div>
        <div style={{ margin: '8px 0' }}>
          <label style={{ display: 'block', marginBottom: '4px' }}>Email:</label>
          <input
            type="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            style={{ padding: '8px', width: '300px' }}
          />
          {errors.email && <p style={{ color: 'red', margin: '4px 0 0 0' }}>{errors.email}</p>}
        </div>
        <button 
          type="submit" 
          style={{ padding: '8px 16px', marginTop: '8px' }}
          disabled={Object.keys(errors).length > 0}
        >
          Submit
        </button>
      </form>
    </div>
  );
}

// 主应用组件
function App() {
  return (
    <div className="App" style={{ maxWidth: '800px', margin: '0 auto', padding: '20px' }}>
      <h1>React Form Handling Example</h1>

      <BasicForm />
      <FormWithValidation />
      <ComplexForm />
      <RealTimeValidationForm />
    </div>
  );
}

export default App;
import React, { useEffect, useRef } from 'react';
import { StaticImage } from 'gatsby-plugin-image';
import styled from 'styled-components';
import { srConfig } from '@config';
import sr from '@utils/sr';
import { usePrefersReducedMotion } from '@hooks';

const StyledAboutSection = styled.section`
  max-width: 900px;

  .inner {
    display: grid;
    grid-template-columns: 3fr 2fr;
    grid-gap: 50px;

    @media (max-width: 768px) {
      display: block;
    }
  }
  .custom-file-input::-webkit-file-upload-button {
    visibility: hidden;
  }
  .custom-file-input {
    ${({ theme }) => theme.mixins.button};
    margin: 10px auto 10px;
    content: 'Select some files';
  }
  .more-button {
    ${({ theme }) => theme.mixins.button};
    margin: 10px auto 10px;
  }
`;
const StyledText = styled.div`
  ul.skills-list {
    display: grid;
    grid-template-columns: repeat(2, minmax(140px, 200px));
    grid-gap: 0 10px;
    padding: 0;
    margin: 20px 0 0 0;
    overflow: hidden;
    list-style: none;

    li {
      position: relative;
      margin-bottom: 10px;
      padding-left: 20px;
      font-family: var(--font-mono);
      font-size: var(--fz-xs);

      &:before {
        content: '▹';
        position: absolute;
        left: 0;
        color: var(--green);
        font-size: var(--fz-sm);
        line-height: 12px;
      }
    }
  }
`;
const StyledPic = styled.div`
  position: relative;
  max-width: 300px;

  @media (max-width: 768px) {
    margin: 50px auto 0;
    width: 70%;
  }

  .wrapper {
    ${({ theme }) => theme.mixins.boxShadow};
    display: block;
    position: relative;
    width: 100%;
    border-radius: var(--border-radius);
    background-color: var(--green);

    &:hover,
    &:focus {
      background: transparent;
      outline: 0;

      &:after {
        top: 15px;
        left: 15px;
      }

      .img {
        filter: none;
        mix-blend-mode: normal;
      }
    }

    .img {
      position: relative;
      border-radius: var(--border-radius);
      mix-blend-mode: multiply;
      filter: grayscale(100%) contrast(1);
      transition: var(--transition);
    }

    &:before,
    &:after {
      content: '';
      display: block;
      position: absolute;
      width: 100%;
      height: 100%;
      border-radius: var(--border-radius);
      transition: var(--transition);
    }

    &:before {
      top: 0;
      left: 0;
      background-color: var(--navy);
      mix-blend-mode: screen;
    }

    &:after {
      border: 2px solid var(--green);
      top: 20px;
      left: 20px;
      z-index: -1;
    }
  }
`;


class Main extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      imageURL: '',
    };

    this.handleUploadImage = this.handleUploadImage.bind(this);
  }
  
  handleUploadImage(ev) {
    ev.preventDefault();

    const data = new FormData();
    data.append('input', this.uploadInput.files[0]);
    data.append('output', this.uploadInput.files[1])
    data.append('filename', this.fileName.value);

    fetch('http://localhost:1000/upload', {
      method: 'POST',
      body: data,
    }).then((response) => {
      response.json().then((body) => {
        this.setState({ imageURL: `http://localhost:8000/${body.file}` });
      });
    });
  }

  render() {
    return (
      <div>
      <form onSubmit={this.handleUploadImage}>
        <div>
          <input ref={(ref) => { this.uploadInput = ref; }} type="file" class="custom-file-input"/>
        </div>
        <div>
          <input ref={(ref) => { this.uploadInput = ref; }} type="file" class="custom-file-input"/>
        </div>
        <br />
        <div>
          <button className='more-button'>Upload</button>
        </div>
      </form>
      </div>
    );
  }
}

const NeuralNetwork = () => {
  const revealContainer = useRef(null);
  const prefersReducedMotion = usePrefersReducedMotion();

  // this.handleUploadImage = this.handleUploadImage.bind(this);
  useEffect(() => {
    if (prefersReducedMotion) {
      return;
    }


    sr.reveal(revealContainer.current, srConfig());
  }, []);

  const skills = ['JavaScript (ES6+)', 'Python', 'React', 'Java', 'SciKit-Learn', 'Natural Language Toolkit, Tensorflow'];

  return (
    <StyledAboutSection id="about" ref={revealContainer}>
      <h2 className="numbered-heading">Understanding Neural Networks</h2>

      <div className="inner">
        <StyledText>
          <div>
            <p>
              Artificial Intelligence is the future of technology as we know it. However, its inner-workings are often unknown, especially by those without a strong mathematical foundation.
              All AI is created under the basis of the human brain, through a model known as a Neural Network. 
            </p>

            <p>
              Fast-forward to today, and I’ve had the privilege of working at{' '}
              <a href="https://transgti.com/">a transportation intelligence company</a>,{' '}
              <a href="https://intuitiontx.com">a start-up tutoring business</a>,{' '}and{' '}
              <a href="https://www.friscoisd.org/departments/independent-study-mentorship/students-parents">a mentorship</a>. My
              main focus these days is building AI tools that increase accessiblity of medical care at my school's Independent Study and Mentorship program.
            </p>

            <p>Here are a few technologies I’ve been working with recently:</p>
          </div>

          <ul className="skills-list">
            {skills && skills.map((skill, i) => <li key={i}>{skill}</li>)}
          </ul>
        </StyledText>
        <Main/>
        <StyledPic>
          <div className="wrapper">
            <StaticImage
              className="img"
              src="../../images/me.jpeg"
              width={500}
              quality={95}
              formats={['AUTO', 'WEBP', 'AVIF']}
              alt="Headshot"
            />
          </div>
        </StyledPic>
      </div>
    </StyledAboutSection>
  );
};

export default NeuralNetwork;

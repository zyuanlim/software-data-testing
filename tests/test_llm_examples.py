from src.llm.llm_examples import extract_cv_data


def test_extract_cv_data():
    test_cv = """
    Jane Smith
    Software Engineering Professional
    email: jane.smith@email.com
    123 Tech Avenue, San Francisco, CA 94105

    PROFESSIONAL EXPERIENCE

    Senior Software Engineer | TechCorp International
    January 2020 - Present
    Led development of cloud-native applications using microservices architecture.
    Managed a team of 5 engineers and implemented CI/CD pipelines reducing deployment time by 40%.

    Software Engineer | Innovation Studios
    March 2017 - December 2019
    Developed full-stack applications using React and Node.js.
    Implemented automated testing frameworks improving code coverage by 75%.

    EDUCATION

    Master of Science in Computer Science
    Stanford University
    2017
    Focus: Artificial Intelligence

    Bachelor of Science in Software Engineering
    University of California, Berkeley
    2015
    Focus: Computer Systems
    """

    result = extract_cv_data(test_cv)

    # Test basic structure
    assert isinstance(result, dict)
    assert result["name"] == "Jane Smith"
    assert result["email"] == "jane.smith@email.com"
    assert "San Francisco" in result["address"]

    # Test experiences
    assert len(result["experiences"]) == 2
    assert result["experiences"][0]["company"] == "TechCorp International"
    assert result["experiences"][0]["position"] == "Senior Software Engineer"
    assert "2020" in result["experiences"][0]["duration"]
    assert "microservices" in result["experiences"][0]["description"].lower()

    # Test education
    assert len(result["education"]) == 2
    assert result["education"][0]["institution"] == "Stanford University"
    assert result["education"][0]["degree"] == "Master of Science"
    assert result["education"][0]["year"] == "2017"
    assert "Artificial Intelligence" in result["education"][0]["major"]

# eWHEP Staffing Package Project: Complete Video Script

## Opening Hook (0:00-0:30)

**"What if I told you that postal workers have been systematically understaffed for years, and management has been using faulty data to justify it? Today, I'm going to show you a suite of tools I built that can expose these discrepancies and help unions fight back with hard data."**

---

## Section 1: The Problem & Inspiration (0:30-3:00)

### The eWHEP Challenge

**"This project was born from a real problem in the postal service. The Electronic Workhour Estimator Program - or eWHEP - is supposed to calculate how many maintenance workers each facility needs. But there's a fundamental flaw in the system."**

### Key Issues:

- **Tour Misrepresentation**: Management often underreports how many tours machines actually run
    - Machine running 3 tours gets recorded as 1-2 tours
    - This directly reduces calculated staffing requirements
- **Data Manipulation**: Manual entry allows for "creative" interpretation
- **Lack of Transparency**: Workers can't easily verify the calculations

### Real-World Impact:

**"When a machine that runs 24/7 gets recorded as running only 8 hours a day, that's not just a paperwork error - that's potentially dozens of missing maintenance positions across a facility."**

---

## Section 2: Contractual Foundation (3:00-5:30)

### Legal Framework

**"This isn't just about numbers - it's about contractual violations that cost workers jobs and compromise safety."**

#### Key Contract Provisions:

- **Article 19**: Management must follow handbooks and manuals
- **MMO-125-20**: Current maintenance workhour estimating guide
- **Article 38.4**: Position posting and filling requirements
- **ASM 531.7**: Staffing requirements and authorizations

#### The Legal Strategy:

1. **Prove Discrepancies**: Show calculated vs. actual staffing needs
2. **Document Violations**: Use concrete data, not opinions
3. **Demand Compliance**: Force management to follow their own procedures
4. **Seek Remedies**: Back pay for bypassed hours, proper staffing levels

---

## Section 3: Project Overview (5:30-7:00)

### The Solution: A Complete Toolkit

**"Instead of fighting management with guesswork, I built a system that uses their own data against them."**

#### Four Core Components:

1. **Machine Checker**: Analyzes individual machine staffing requirements
2. **WebEOR Data Visualizer**: Processes operational data to show actual usage
3. **RFI Builder**: Generates legal requests for information
4. **Grievance Form**: Creates professional grievance documentation

### Why This Approach Works:

- **Data-Driven**: Uses management's own numbers
- **Legally Sound**: Built on contract provisions
- **User-Friendly**: No technical expertise required
- **Comprehensive**: Covers the entire grievance process

---

## Section 4: Technical Deep Dive (7:00-12:00)

### Tool 1: Machine Checker (PowerShell Application)

**"This is the heart of the system - a PowerShell application that reads Excel data and calculates proper staffing."**

#### Key Features:

- **CSV Integration**: Reads machine and class code mappings
- **Dynamic Configuration**: Adapts to different machine types and MMOs
- **Staffing Calculations**: Matches operational parameters to lookup tables
- **Report Generation**: Creates comprehensive HTML reports with discrepancies

#### Technical Innovation:

- **Highlight Matching**: Visually shows which lookup table rows match your machines
- **Original vs. Standardized Values**: Tracks when values are adjusted for compliance
- **Automatic Calculations**: Converts operational data into staffing requirements

### Tool 2: WebEOR Data Visualizer

**"This tool takes raw operational data and creates compelling visualizations that show actual machine usage."**

#### Capabilities:

- **Multi-File Processing**: Combines and deduplicates CSV files
- **Machine Analytics**: Calculates tours per day and days per week from real data
- **Performance Metrics**: Shows efficiency and utilization patterns
- **Export Functions**: Generates reports for grievance documentation

### Tool 3: RFI Builder

**"Before you can challenge staffing, you need the right documents. This tool generates legally compliant requests."**

#### Features:

- **Template-Based**: Pre-built for eWHEP challenges
- **Legal References**: Includes relevant contract citations and case law
- **Professional Formatting**: Matches USPS document standards
- **Automatic Dating**: Handles due dates and timestamps

### Tool 4: Grievance Form Generator

**"The final piece - converting your data into a professional grievance that management has to take seriously."**

#### Integration Points:

- **Report Import**: Directly reads Machine Checker and WebEOR reports
- **Auto-Population**: Fills grievance language based on imported data
- **Legal Compliance**: Includes proper contract citations and remedies
- **PDF Export**: Creates print-ready documentation

---

## Section 5: Real-World Application (12:00-15:00)

### The Workflow in Action

**"Let me walk you through how this actually works in practice."**

#### Step 1: Data Collection

1. Request WebEOR data from management
2. Import into WebEOR Visualizer
3. Generate machine utilization report

#### Step 2: Staffing Analysis

1. Load machine data into Machine Checker
2. Configure parameters based on actual operations
3. Generate staffing comparison report

#### Step 3: Documentation Request

1. Use RFI Builder to request eWHEP package
2. Submit professionally formatted request
3. Document management's response (or lack thereof)

#### Step 4: Grievance Filing

1. Import all reports into Grievance Form
2. Review auto-generated language
3. File comprehensive grievance with supporting data

### Case Study Results:

**"In testing, this approach identified significant understaffing that management couldn't dispute because we used their own data and their own formulas."**

---

## Section 6: The Bigger Picture (15:00-17:00)

### Why This Matters

**"This isn't just about one contract or one union - it's about using technology to level the playing field."**

#### Broader Implications:

- **Transparency**: Forces management to show their work
- **Accountability**: Creates paper trails that can't be ignored
- **Empowerment**: Gives workers tools to fight back effectively
- **Innovation**: Shows how unions can adapt to modern challenges

### The Future:

- **Scalability**: Can be adapted to other crafts and contracts
- **Automation**: Reduces the burden on union stewards
- **Standardization**: Creates consistent, professional documentation
- **Training**: Builds technical literacy in the labor movement

---

## Section 7: Technical Philosophy (17:00-19:00)

### Design Principles

**"Every tool was built with working people in mind, not IT departments."**

#### User-Focused Design:

- **No Installation Required**: HTML tools run in any browser
- **Visual Feedback**: Color coding and progress indicators
- **Error Handling**: Graceful failure with helpful messages
- **Documentation**: Every feature is explained in plain language

#### Data Integrity:

- **Preservation**: Original values are never lost
- **Traceability**: Every calculation can be verified
- **Reproducibility**: Results are consistent and documentable
- **Validation**: Multiple checks prevent errors

---

## Section 8: Legal Strategy Deep Dive (19:00-21:00)

### Contract Enforcement Theory

**"The beauty of this approach is that we're not asking for favors - we're demanding compliance with existing agreements."**

#### Strategic Elements:

1. **Article 19 Violations**: Management must follow their own procedures
2. **Staffing Package Requirements**: MMO-125-20 compliance is mandatory
3. **Hour-for-Hour Remedies**: Bypassed work equals compensable time
4. **Prospective Relief**: Fix the system, not just pay damages

#### Arbitration Advantages:

- **Objective Standards**: Arbitrators can verify calculations
- **Clear Violations**: Black and white contract breaches
- **Concrete Remedies**: Specific hours and dollar amounts
- **Precedent Value**: Decisions apply facility-wide

---

## Section 9: Implementation Strategy (21:00-23:00)

### Rolling Out the Tools

**"The technical part is actually the easy part - the real challenge is organizational."**

#### Training Requirements:

- **Basic Computer Skills**: File management and web browsers
- **Contract Knowledge**: Understanding relevant articles
- **Data Interpretation**: Reading reports and identifying issues
- **Grievance Procedure**: Following proper filing protocols

#### Support Structure:

- **Documentation**: Comprehensive user guides
- **Video Tutorials**: Step-by-step walkthroughs
- **Troubleshooting**: Common issues and solutions
- **Updates**: Regular improvements based on feedback

### Scalability Considerations:

- **Local Adaptation**: Tools can be customized for specific facilities
- **Regional Deployment**: Coordinated implementation across areas
- **National Impact**: Potential for system-wide change

---

## Section 10: Challenges and Limitations (23:00-24:30)

### Technical Constraints

**"No tool is perfect, and it's important to understand the limitations."**

#### Current Limitations:

- **Data Dependency**: Tools are only as good as the input data
- **Format Changes**: USPS may modify report structures
- **Access Issues**: Management may restrict data availability
- **Complexity**: Some situations require manual analysis

#### Mitigation Strategies:

- **Multiple Data Sources**: Don't rely on single reports
- **Version Control**: Track changes in USPS systems
- **Legal Pressure**: Use contract enforcement to ensure access
- **Human Judgment**: Tools support, don't replace, expertise

---

## Conclusion: The Path Forward (24:30-26:00)

### Immediate Impact

**"These tools are available now and can make an immediate difference in ongoing staffing fights."**

### Long-Term Vision

**"But the real goal is bigger than any one grievance or any one contract. This is about showing the labor movement what's possible when we embrace technology and use data as effectively as management does."**

#### Call to Action:

1. **Download and Test**: Get familiar with the tools
2. **Identify Opportunities**: Look for staffing discrepancies
3. **Build Expertise**: Train stewards and officers
4. **Share Results**: Document successes and failures
5. **Improve Together**: Contribute to ongoing development

### Final Thought:

**"Management has been using technology against workers for decades. It's time we turned the tables and used their own tools to hold them accountable. The contract is on our side - we just need to enforce it with the same precision they use to violate it."**

---

## Appendix: Resource List

### Download Links:

- Machine Checker PowerShell Script
- WebEOR Data Visualizer HTML
- RFI Builder HTML
- Grievance Form HTML

### Reference Documents:

- MMO-125-20 (Maintenance Workhour Estimating Guide)
- Article 19 (Handbooks and Manuals)
- ASM 531.7 (Staffing Requirements)
- Sample Grievance Language

### Contact Information:

- Technical Support
- Legal Questions
- Training Resources
- Feedback and Suggestions

---

**Total Runtime: Approximately 26 minutes**

_Note: This script is designed to be modular - sections can be recorded separately and combined, or the full script can be used for a comprehensive presentation._
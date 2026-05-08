# Integrated Planning Document for an Amateur Basketball Platform and Smart Scoreboard

> Version: English edition

> **Document purpose:**
> This document is an integrated requirements specification for AI development tools such as Gemini, ChatGPT, Claude, Cursor, and Copilot. It defines the product intent, feature scope, technical structure, implementation priorities, security rules, permission model, testing expectations, and completion criteria in one consistent reference.
>
> The document consolidates accumulated drafts from prior discussions. Duplicate expressions have been removed, and details that were easy to lose across iterations have been restored and organized.

---

## 0. Principles for Using AI Development Tools

AI tools must treat this document as the single source of truth for development, not as a casual reference.

### 0.1 Mandatory Principles for AI Developers

1. Do not arbitrarily reduce, omit, or reinterpret explicitly stated user requirements.
2. Before implementing a feature, identify which section of this document the feature belongs to.
3. If a new request conflicts with an existing requirement, clearly state the conflict and ask for confirmation.
4. Generated code must include maintainable architecture, logging, tests, permission control, and error handling, not just working code.
5. Do not mix MVP features with commercial expansion features.
6. Break complex features into small, staged implementation units.
7. Design the UI so non-technical users, children, and elderly users can operate it intuitively.
8. Use defensive programming for any feature involving payments, personal data, permissions, or official game records.

---

## 1. Project Overview

### 1.1 Project Name

**Amateur Basketball Integrated Platform and Smart Scoreboard**

### 1.2 One-line Definition

A web-based O2O platform that integrates amateur basketball game operation, scoreboard control, record management, team and player databases, community features, pickup game and guest matching, gym reservation, document automation, and a payment/credit system.

### 1.3 Core Objectives

| Area | Objective |
|---|---|
| Game operation | Digitize paper score sheets and control real-time scoreboard and record entry through the web. |
| Data management | Manage teams, players, leagues, tournaments, game results, gyms, and applications through structured CRUD features. |
| Community | Provide a space where teams, players, scorekeepers, referees, organizers, and general users can communicate. |
| Matching | Connect pickup games, guest players, referees, and scorekeepers. |
| Document automation | Digitize existing event documents through PDF upload, parsing, export, and printing. |
| Commercialization | In Phase 2, expand into gym reservations, participation fee payments, credits, points, and advertising revenue. |

### 1.4 Service Characteristics

- Web-based integrated platform
- Mobile-first responsive web design
- Free open beta during the MVP stage
- Later expansion into O2O gym reservations, payments, credits, and advertising based on traffic and user feedback
- Global frontend deployment through Vercel
- Separate backend server based on FastAPI

---

## 2. Development and Deployment Strategy

## 2.1 Phase 1: Open Beta / MVP

Phase 1 starts as a free service. The key principle is practical field usability.

### Phase 1 Goals

1. Provide a scoreboard that can be used immediately by clubs, small tournaments, and casual basketball groups.
2. Provide a digital score sheet that lets scorekeepers enter game records by clicking.
3. Provide basic CRUD management for teams, players, leagues, and tournaments.
4. Provide community, Q&A, notices, FAQ, and manual pages.
5. Build the basic structure for PDF upload and PDF export.
6. Provide selected team intranet features.
7. Distribute to nearby amateur basketball users and collect UI/UX feedback.
8. Validate that non-technical users can use the service easily.

### Phase 1 Feature Scope

| Area | Features |
|---|---|
| Scoreboard | Game control panel, game status viewer, digital score sheet, result screen |
| Data management | Team, player, league, tournament, and game result CRUD |
| Community | Notices, discussion board, comments, Q&A, FAQ, user manual |
| Team management | Team roster, attendance check, practice attendance vote, uniform/equipment survey |
| Documents | PDF template download, PDF export, basic PDF parsing |
| Permissions | Guest, user, team manager, system administrator roles |
| Accessibility | Large buttons, icon-centered UI, tooltips, mobile/tablet optimization |
| Display | Dedicated scoreboard route for a 75-inch TV or external monitor |

---

## 2.2 Phase 2: Commercialization Blueprint

Phase 2 begins after enough users have been acquired and real demand for reservations, matching, and operations has been validated.

### Phase 2 Goals

1. Connect gym reservation, electronic agreement, payment, and refund policy.
2. Introduce participation fee payments and credit payments for pickup games.
3. Provide a point/credit-based wallet UI.
4. Generate additional revenue through ad banners.
5. Integrate Kakao AlimTalk, SMS, and email notifications.
6. Strengthen security with mobile phone verification, email verification, bank account verification, and payment card registration.
7. Introduce reviews, ratings, and manner score systems.
8. Reflect escrow-like protection and no-show prevention policies.

### Phase 2 Feature Scope

| Area | Features |
|---|---|
| Payment | Payment gateway integration, participation fee payment, gym reservation payment, credit recharge |
| Security verification | Mobile phone verification, email verification, bank account verification, payment card registration |
| O2O gym reservation | Gym search, reservation calendar, electronic agreement, payment, refund |
| Economy system | Point rewards, credit usage, wallet UI, settlement |
| Advertising | Banner ads on home, discussion list, and my page |
| Trust system | Gym reviews, participant manner evaluation, manner score |
| Notifications | Kakao AlimTalk, SMS, email, game reminders |

---

## 3. Technology Stack and Infrastructure Architecture

## 3.1 Overall Architecture

The system must separate frontend and backend. Start with a simple separated architecture, while keeping the structure extensible toward microservices later.

```text
[User Device]
  |- Mobile Browser
  |- Tablet Browser
  |- PC Browser
  |- Display Browser / HDMI TV

        ↓ HTTPS

[Frontend: Vue.js + TypeScript]
  |- Vercel Hosting
  |- Responsive UI
  |- Scoreboard Control Panel
  |- Display Route
  |- Community / Dashboard

        ↓ REST / WebSocket

[Backend: FastAPI]
  |- Auth / RBAC
  |- Game State API
  |- Score Event API
  |- Team / Player / League API
  |- PDF Parsing / Export API
  |- Payment / Credit API
  |- Notification API
  |- Hardware Packet API

        ↓

[Database Layer]
  |- PostgreSQL + SQLAlchemy
  |- MongoDB
```

---

## 3.2 Frontend

### Required Stack

- Vue.js
- TypeScript
- Vercel deployment
- Responsive web design
- Mobile-first design
- Component-based UI
- Dedicated scoreboard display route

### Frontend Implementation Principles

1. Prefer the Vue Composition API.
2. Separate components by responsibility.
3. Prioritize touch operation for the game control panel.
4. Prioritize TV display readability for the scoreboard view.
5. Admin pages must support tables, filters, sorting, search, and bulk operations.
6. Use a WYSIWYG editor for rich community posts when appropriate.
7. Apply permission guards at the router level.
8. Provide a global error handling structure or error boundary equivalent.

### Example Frontend Routes

```text
/
/login
/signup
/dashboard

/games
/games/:gameId/control
/games/:gameId/record
/games/:gameId/display
/games/:gameId/result

/teams
/teams/:teamId
/teams/:teamId/intranet
/players
/leagues
/tournaments
/tournaments/:tournamentId/apply

/pickup
/referee-jobs
/scorekeeper-jobs
/community
/community/:postId

/gyms
/gyms/:gymId
/gyms/:gymId/reserve

/wallet
/points
/credits

/notices
/manual
/faq
/qna
/about
/contact

/admin
/admin/users
/admin/teams
/admin/games
/admin/tournaments
/admin/payments
/admin/logs
```

---

## 3.3 Backend

### Required Stack

- FastAPI
- Python
- Docker
- Nginx reverse proxy
- Cloud server or VPS deployment
- REST API
- WebSocket or Server-Sent Events for real-time game state synchronization
- Logging middleware
- Authentication and authorization middleware
- File upload and validation middleware

### Backend Implementation Principles

1. Apply RBAC at the API level.
2. Every state-changing API must log the requester, request time, previous state, and next state.
3. Payments, credits, points, and game records must preserve transaction integrity.
4. File uploads must validate MIME type, extension, file size, and malicious content risk.
5. PDF parsing results must pass through a review screen before being committed to the database.
6. Separate external API integrations into adapter or service layers.
7. Separate hardware packet generation into an independent module.

---

## 3.4 Database

### PostgreSQL + SQLAlchemy

Use PostgreSQL for relational data that requires consistency and integrity.

#### Data Stored in PostgreSQL

- User accounts
- Roles and permissions
- Team information
- Player profiles
- Team rosters
- League structures
- Tournament brackets
- Tournament information
- Participation applications
- Gym information
- Reservation records
- Payment history
- Credit balances
- Point summaries
- Admin settings

### MongoDB

Use MongoDB for unstructured data, logs, and large event-based data.

#### Data Stored in MongoDB

- Play-by-play game logs
- Real-time game state snapshots
- Box score statistics logs
- Community post body content
- Comments and replies
- Chat data
- File metadata
- Detailed point earning logs
- System event logs
- Original AI parsing data and parsed result logs

---

## 3.5 AI and Document Processing

### PDF Processing

Prioritize the following libraries and tools:

- `pdfplumber`: strong for extracting tables
- `PyMuPDF`: strong for PDF rendering, text extraction, and image handling
- OpenAI API or open-source LLMs: document interpretation, field extraction, and missing value detection

### Document Processing Principles

1. Provide standard PDF templates.
2. Users can upload PDFs such as tournament results, score sheets, and gym rental agreements.
3. AI must extract dates, locations, participation fees, team names, player names, scores, benefits, and rules from PDFs.
4. Missing values must be displayed as `N/A`.
5. `N/A` values or low-confidence values must be routed to manual input and review.
6. Parsed data must not be finalized in the production database before review is complete.
7. Log the original file, parsing result, reviewer, and review timestamp.
8. Team information, player profiles, tournament information, game results, and box scores must be exportable to PDF and printable immediately.

---

## 3.6 Third-party Integrations

Keep the architecture open for the following Phase 2 integrations.

| Integration target | Purpose |
|---|---|
| Payment gateway | Participation fee, gym rental fee, credit recharge |
| Toss Payments | Candidate domestic payment provider |
| PortOne | Candidate multi-PG integration provider |
| Kakao AlimTalk | Payment completion, game reminder, matching acceptance notifications |
| SMS API | Phone verification and urgent notifications |
| Email API | Signup verification, notices, receipts |
| Map/GPS API | Nearby gyms and pickup game recommendations |
| Advertising platform | Banner ad monetization |

---

## 4. User Roles and Permissions

## 4.1 Role Definitions

| Role | Description |
|---|---|
| Guest | Can view public information. Writing, applications, edits, and downloads are restricted. |
| User | Can write posts, comment, apply, scrap information, and use My Page after signup. |
| Player | A player assigned to a specific team. Can check personal game records and team schedules. |
| Team Manager | Can manage team information, roster, guest acceptance, and team intranet. |
| Scorekeeper | Can enter scores, fouls, and player records in the game control panel. |
| Referee | Can check assigned games and apply to referee job posts. |
| Tournament Admin | Can manage tournaments, leagues, schedules, brackets, and participation approvals. |
| Gym Owner/Admin | Can manage gym information, available reservation time, and reservation approvals. |
| System Admin | Can manage all users, permissions, data, payments, logs, reports, and environment settings. |

---

## 4.2 Permission Principles

1. Public viewing should be as open as possible.
2. Writing, editing, deleting, downloading, payment, approval, and sensitive data viewing require permissions.
3. Sensitive information must be blurred or masked for unauthorized users.
4. Permission checks must also be enforced in APIs.
5. Frontend router guards alone are not sufficient for authorization.
6. System administrators must be able to audit permission change history.

---

## 4.3 Sensitive Data Handling

### Examples of Sensitive Data

- Phone numbers
- Full addresses
- Bank account information
- Payment card information
- Identity verification information
- Player identification information
- Gym contract-related information

### Handling Principles

1. Apply encryption where necessary before storing data.
2. Store passwords only as one-way hashes.
3. Mask or blur phone numbers, addresses, and similar data by permission level.
4. Never store raw payment card information directly.
5. Log sensitive data access history.
6. Control download permissions separately.

---

## 5. Core Menus and Feature Specifications

## 5.1 Common and User Area

### 5.1.1 Home

The home screen is both the service entrance and a real-time overview board.

#### Required Features

- Platform introduction
- Major tournament news
- Real-time game status summary
- Ongoing game cards
- Upcoming game cards
- Popular community posts
- Nearby pickup game recommendations
- Nearby gym recommendations
- Notice summary
- Banner ad area for Phase 2

#### UX Requirements

- Core information must be visible immediately on mobile.
- Guests must be able to view major public information.
- Live games must be visually prominent.

---

### 5.1.2 Account Management

#### Required Features

- Login
- Signup
- Logout
- Password reset
- Profile editing
- Permission request
- Team join request
- Admin permission approval
- Permission control for writing, editing, and downloading

#### Phase 2 Extensions

- Mobile phone verification
- Email verification
- Bank account verification
- Payment card registration
- Social login
- Two-factor authentication

---

### 5.1.3 My Page / Dashboard

#### Required Features

- My team list
- My joined tournaments
- My applications
- My pickup games
- My guest applications
- Scrapped information
- My posts and comments
- Point and credit status
- Notifications
- Permission status

---

## 5.2 Game Operation and Scoreboard Area

This is the core of the service and must be implemented first.

### 5.2.1 Game Creation and Basic Settings

#### Required Input Values

- Home team
- Away team
- Game date and time
- Venue
- Quarter length
- Number of quarters
- Overtime rule
- Team foul limit
- Shot clock availability
- Scorekeeper
- Referee
- Tournament or league association

#### Validation Conditions

- A game cannot start without both teams.
- Quarter length must be a positive number.
- Team information must be saved before assigning players.
- Only authorized users can create or edit games.
- Changes after game start must be logged.

---

### 5.2.2 Game Control Panel

The game control panel acts as a web-based scoreboard controller.

#### Required Features

- Start/pause/resume/end game
- Quarter selection
- Game clock adjustment
- Home and away score controls
- 1-point, 2-point, and 3-point scoring buttons
- Score correction
- Team foul increase/decrease
- Timeout count management
- Overtime handling
- Undo/redo for recent actions
- Manual correction reason input
- Real-time synchronization to display route
- Logging of every score and state change

#### UX Requirements

- Buttons must be large enough for tablet and mobile touch usage.
- Accidental touches must be reduced through sufficient spacing.
- High-frequency actions such as score entry and foul entry must be accessible within one or two taps.
- Important actions such as game end and reset require confirmation.
- Undo must be easy to access.

---

### 5.2.3 Digital Score Sheet

This replaces handwritten scorekeeping with click-based record entry.

#### Required Features

- Display rosters by home and away teams
- Select player and enter 1, 2, or 3 points
- Enter free throw attempts and makes
- Enter personal fouls
- Enter team fouls
- Enter rebounds, assists, steals, blocks, and turnovers
- Automatically update team score after player scoring input
- Automatically update player statistics
- Save play-by-play logs
- Synchronize with database
- Support post-game correction

#### Input Example

If a scorekeeper clicks `2 points` next to player number 3 on the away team:

1. Away team score increases by 2.
2. Player number 3 receives 2 points in the box score.
3. A play-by-play event is created.
4. The scoreboard display route updates in real time.
5. The action is logged.

#### Validation Conditions

- A player not included in the roster cannot receive a record.
- Scores cannot become negative.
- Fouls cannot become negative.
- Correction after game end requires a correction reason.

---

### 5.2.4 Game Status Viewer

#### Required Display Information

- Home team name
- Away team name
- Home score
- Away score
- Remaining time
- Current quarter
- Team fouls
- Timeouts
- Main player statistics
- Real-time box score
- Possession or attack direction when needed

#### UI Requirements

- Must be readable from a distance.
- Use a high-contrast layout, such as black background with yellow/red/white text.
- Avoid excessive information on the TV display.
- Use a separate statistics area for detailed box score information.
- Font size must be optimized for 75-inch TV output.

---

### 5.2.5 Dedicated Scoreboard Display Route

#### Required Conditions

- Provide a separate route such as `/games/:gameId/display`.
- This route must be usable in full-screen browser mode.
- It must be displayable through HDMI on a TV or large monitor.
- The screen must update immediately when the control panel changes.
- It must avoid unnecessary buttons or admin UI.
- It must support landscape layout first.
- It must preserve readability at a distance.

---

### 5.2.6 Game Result Screen

#### Required Features

- Final score
- Winner/loser summary
- Quarter-by-quarter score
- Team box score
- Player box score
- Play-by-play log
- MVP or top player summary
- Comment and discussion area
- PDF export
- Share link

---

## 5.3 Database Management Area

All management pages must support CRUD as a baseline.

### 5.3.1 Team Information

#### Required Features

- Team list
- Search
- Filtering by region, level, gender, age group, and activity day
- Sorting
- Team detail page
- Team location
- Awards and history
- Roster
- Team manager information
- Team introduction
- Recruitment status
- Team profile image
- Team schedule

#### Sensitive Information

- Team manager contact information is visible only to authorized users.
- Internal roster information is visible only to authorized team members or admins.

---

### 5.3.2 Player Information

#### Required Features

- Player list
- Player profile
- Name, nickname, jersey number, height, position, team, career, awards
- Filter by position, team, height, and region
- Statistics summary
- Game history
- Profile image

#### Personal Data Protection

- Phone numbers and full addresses must be blurred or hidden from non-admin users.
- Sensitive information must never be exposed in API responses to unauthorized users.
- Exporting player data requires a separate permission check.

---

### 5.3.3 League Information

#### Required Features

- Ongoing league list
- League detail information
- Participating teams
- Group stage standings
- Tournament bracket
- Pyramid view bracket
- Win/loss table
- Points table
- Game schedule
- Result entry
- Rule document attachment
- League notice

---

### 5.3.4 Tournament Status and Applications

#### Required Features

- Upcoming tournament list
- Tournament detail page
- Participation conditions
- Registration period
- Participation fee
- Venue
- Format
- Online application form
- Application status
- Approval/rejection status
- Payment status for Phase 2
- Participant list
- Admin approval page

---

## 5.4 Data and AI Document Automation Area

### 5.4.1 PDF Template Provision

Provide downloadable standardized templates.

#### Template Examples

- Game score sheet
- Tournament result sheet
- Team roster form
- Player profile form
- Gym reservation agreement
- Participation application form
- Settlement report

---

### 5.4.2 Automatic PDF Parsing

#### Required Features

- Upload PDF file
- Extract text and tables
- AI-assisted field extraction
- Extract date, location, team name, player name, score, participation fee, benefit, and rule data
- Mark missing fields as `N/A`
- Show parsing result preview
- Route missing or low-confidence values to manual review
- Save only after user confirmation
- Log original file, parsed result, reviewer, and confirmation time

#### Validation Conditions

- Block unsupported file extensions.
- Validate MIME type.
- Limit file size.
- Do not trust parsed values blindly.
- Require manual review before database reflection.
- Keep raw parsing logs for debugging.

---

### 5.4.3 PDF Export and Printing

#### Required Features

- Export team information to PDF
- Export player profiles to PDF
- Export tournament status to PDF
- Export game result and box score to PDF
- Export team roster to PDF
- Export attendance and vote results to PDF
- Print immediately from browser
- Include permission control for downloads

---

## 5.5 Community and Matching Area

### 5.5.1 Pickup Game / Guest Application

#### Workflow

1. A team manager creates a recruitment post.
2. The post specifies date, time, gym, required position, skill level, participation fee, and number of participants.
3. A user applies.
4. The team manager accepts or rejects.
5. If accepted, the user is temporarily added to the roster as a guest.
6. Notification is sent.
7. In Phase 2, payment and refund rules are applied.

#### Required Features

- Recruitment post creation
- Region and schedule filtering
- Position and skill-level filtering
- User application
- Team manager approval
- Temporary roster registration
- Application status tracking
- Notification
- Participation fee configuration for Phase 2
- Credit payment for Phase 2

---

### 5.5.2 Referee / Scorekeeper Recruiting

Amateur events often lack referees and scorekeepers, so matching support is required.

#### Required Features

- Referee recruitment posts
- Scorekeeper recruitment posts
- Location, date, compensation, and required experience fields
- Application
- Approval/rejection
- Assignment confirmation
- Completion confirmation
- Review or rating after completion for Phase 2

---

### 5.5.3 Free Discussion Board

#### Required Features

- Post CRUD
- Comment CRUD
- Replies
- Like/dislike or recommendation system
- Image upload
- Document attachment
- File download
- WYSIWYG editor
- Report post
- Report user
- Popular posts
- Search
- Category filtering

---

### 5.5.4 Community Safety Features

- Spam prevention
- Report handling
- Admin moderation
- Content hiding
- User suspension
- Rate limiting
- Malicious file upload prevention
- Macro and bot activity detection

---

## 5.6 Team Intranet Area

### 5.6.1 Standard Team Roster

#### Required Features

- Team member list
- Name, phone number, address, jersey number, position, uniform size, join date, membership fee status
- Excel export
- PDF export
- Member search
- Filtering
- Role assignment
- Active/inactive status management
- Emergency contact field

#### Security Conditions

- Only team managers and authorized admins can view sensitive information.
- Phone numbers and addresses must be encrypted or masked where necessary.
- Export history must be logged.

---

### 5.6.2 Activity and Vote Management

#### Required Features

- Practice attendance vote
- Tournament participation survey
- Uniform size survey
- Equipment purchase vote
- Dinner or event vote
- Result statistics
- Attendance history
- Participation rate summary
- Team notice

---

## 5.7 O2O Gym Reservation Area

This area is mainly a Phase 2 feature, but data models and routing should be prepared early.

### 5.7.1 Gym Information

#### Required Features

- Gym list
- Map view
- Gym detail page
- Address
- Facility photos
- Court count
- Parking availability
- Shower room availability
- Equipment availability
- Available reservation time
- Rental fee
- Gym manager contact information
- Review summary

---

### 5.7.2 Reservation Application Process

#### Workflow

1. User selects gym.
2. User selects date and time.
3. User reviews fee and rules.
4. User agrees to electronic terms.
5. User submits reservation.
6. Payment is processed.
7. Gym manager approves or auto-confirms.
8. Notification is sent.
9. Refund and cancellation rules are applied if needed.

#### Required Features

- Reservation calendar
- Time slot management
- Fee calculation
- Electronic agreement
- Payment link
- Approval status
- Cancellation request
- Refund status
- No-show policy
- Reservation history

---

### 5.7.3 Reviews, Ratings, and Manner Score

#### Required Features

- Gym review after use
- Facility rating
- Cleanliness rating
- Price satisfaction rating
- Participant manner evaluation after pickup games
- Bad manner report
- Good manner evaluation
- Manner score reflected in profile
- Admin review of abusive reports

---

## 5.8 Points, Credits, and Advertising Area

These are Phase 2 commercialization features.

### 5.8.1 Point System

#### Point Reward Examples

- Attendance check
- Writing a post
- Writing a comment
- Joining a game
- Completing scorekeeper work
- Writing a review
- Inviting a friend

#### Abuse Prevention

- Daily earning limit
- API rate limiting
- Duplicate action prevention
- Macro detection
- Suspicious activity logging
- Admin audit screen

---

### 5.8.2 Credit System

#### Required Features

- Credit recharge
- Credit usage
- Credit refund
- Wallet UI
- Transaction history
- Payment failure handling
- Transaction rollback
- Balance lock during payment
- Admin adjustment history

---

### 5.8.3 Banner Advertising

#### Candidate Placements

- Home screen
- Discussion board top and bottom
- My Page
- Game result page
- Tournament list
- Pickup game list

#### Principles

- Do not interfere with core game control.
- Do not show ads on the scoreboard display route.
- Record exposure and click logs.
- Allow admin control over ad status.

---

## 5.9 Customer Support and Guide Area

### 5.9.1 Notices

#### Required Features

- Platform update notices
- Tournament rule change notices
- Service maintenance notices
- Attached files
- Important notice pinning
- Admin-only writing permission

---

### 5.9.2 Manual

#### Required Content

- How to use the game control panel
- How to enter a digital score sheet
- How to connect the scoreboard display
- How to upload and review PDF parsing results
- How to apply to a tournament
- How to manage a team roster
- Screenshots and step-by-step guides

---

### 5.9.3 FAQ

#### Example Topics

- Can I use the scoreboard for free?
- Can I use it on a tablet?
- How do I connect it to a TV?
- Who can edit game records?
- How is personal information protected?
- How do I apply as a guest player?
- How do I upload a PDF?

---

### 5.9.4 Q&A / One-on-one Inquiry

#### Required Features

- Private inquiry board
- Image attachment
- File attachment
- Admin reply
- Status values: received, in progress, completed
- Email or notification on reply
- User inquiry history

---

### 5.9.5 About Us / Contact

#### Required Content

- Development team introduction
- Service vision
- Contact information
- Sponsorship information
- Partnership inquiry
- Terms of service
- Privacy policy

---

## 6. UI/UX Design Guidelines

## 6.1 Overall UI Principles

1. Prioritize mobile-first design.
2. Make frequently used buttons large and clear.
3. Use intuitive icons with text labels.
4. Provide tooltips for complex forms.
5. Keep information hierarchy clear.
6. Avoid hiding important actions too deeply.
7. Use cards and tables appropriately.
8. Provide dark mode and light mode.
9. Support Korean and English language switching.
10. Preserve accessibility for non-technical users.

---

## 6.2 Game Control Panel UI

### Requirements

- Large touch-friendly buttons
- Clear separation between home and away teams
- Color distinction for score, foul, timeout, and clock controls
- Confirmation modal for dangerous actions
- Undo button visible at all times
- Real-time operation log area
- Tablet landscape optimization
- Minimal scrolling during game operation

---

## 6.3 Scoreboard View UI

### Requirements

- Black or very dark background
- Yellow, red, white, or similarly high-contrast text
- Very large score display
- Large remaining time display
- Simple layout
- No unnecessary buttons
- Full-screen support
- Readability from a distance
- 75-inch TV layout optimization

---

## 6.4 Data Management UI

### Requirements

- Search
- Filter
- Sort
- Pagination
- Bulk actions
- Table and card view toggle
- Clear create/edit/delete buttons
- Export button
- Permission-based hidden or disabled actions

---

## 6.5 Accessibility and Convenience Features

### Required Features

- Large tap targets
- Tooltip guide
- Clear error messages
- Loading indicators
- Empty state messages
- Dark/light theme toggle
- Korean/English language mode
- Responsive layout for mobile, tablet, and PC
- Real-time clock synchronization based on reliable time source where needed

---

## 7. Hardware and Communication Integration Guidelines

## 7.1 Web Display Mirroring

The first practical approach is to use a cost-effective 75-inch TV or monitor with a durable acrylic or polycarbonate guard.

### Implementation Method

- Open the scoreboard display route in a browser.
- Connect the PC, tablet, or small device to a TV through HDMI.
- Use full-screen browser mode.
- Synchronize the control panel and display route in real time.

### Requirements

- Dedicated display route
- High-contrast UI
- Large font size
- Landscape layout
- No admin controls on display
- Real-time synchronization
- Stable operation during long games

---

## 7.2 Expansion for Commercial Scoreboard Integration

Prepare the backend structure for future integration with low-cost commercial LED scoreboards.

### Communication Candidates

- RS-485 wired communication
- RF wireless module
- Serial communication bridge
- USB-to-RS485 adapter
- Backend hardware gateway module

### Example Hex Packet Structure

```text
[START_CODE][HOME_SCORE][AWAY_SCORE][REMAINING_TIME][QUARTER][TEAM_FOULS][CHECKSUM][END_CODE]
```

Example:

```text
0x02 0x48 0x55 0x41 0x70 0x05 0x00 0x04 0x03 0x7A 0x03
```

### Implementation Principles

1. Do not hard-code the packet structure inside business logic.
2. Separate packet generation into a module.
3. Make the protocol editable after reverse engineering.
4. Log every transmitted packet.
5. Provide retry and failure handling.
6. Allow the web scoreboard to work even if external hardware integration fails.

---

## 8. Initial Data Model Draft

The following model is a draft. AI developers may refine the fields during implementation, but must preserve the business intent.

## 8.1 Core Entities

| Entity | Purpose |
|---|---|
| User | Account, authentication, profile, permissions |
| Role | Permission grouping |
| Team | Amateur basketball team |
| Player | Player profile and statistics |
| TeamRoster | Relationship between teams and players |
| League | League information |
| Tournament | Tournament information |
| Game | Game schedule and status |
| GameEvent | Play-by-play event |
| BoxScore | Aggregated game statistics |
| Gym | Gym information |
| Reservation | Gym reservation |
| Payment | Payment transaction |
| CreditWallet | Credit balance |
| PointLog | Point earning and usage history |
| Post | Community post |
| Comment | Comment and reply |
| FileAsset | Uploaded file metadata |
| Notification | Notification record |
| AuditLog | System audit log |

---

## 8.2 GameEvent Example

```json
{
  "game_id": "game_001",
  "event_type": "score",
  "team_id": "away_team_001",
  "player_id": "player_003",
  "quarter": 2,
  "game_clock": "05:32",
  "points": 2,
  "previous_home_score": 34,
  "previous_away_score": 29,
  "next_home_score": 34,
  "next_away_score": 31,
  "created_by": "scorekeeper_001",
  "created_at": "2026-05-08T12:00:00+09:00"
}
```

### GameEvent Principles

1. Every score change must create an event.
2. Every correction must create a separate correction event.
3. Do not delete event history casually.
4. Use event history as the basis for reconstructing game flow.
5. Store high-frequency logs in MongoDB when appropriate.

---

## 8.3 Payment / Credit Principles

### Required Conditions

1. Prevent duplicate payment processing.
2. Lock balance during credit usage.
3. Roll back on payment failure.
4. Keep payment logs and credit logs separately.
5. Keep original payment gateway response logs.
6. Let administrators review abnormal transactions.

---

## 9. API Design Principles

## 9.1 Common API Principles

1. Use RESTful URL structure.
2. Use clear request and response schemas.
3. Validate input values with Pydantic.
4. Return standardized error responses.
5. Apply authentication and authorization middleware.
6. Leave audit logs for all state-changing APIs.
7. Separate read APIs and write APIs where useful.
8. Prepare WebSocket or SSE for real-time game state.

---

## 9.2 API Examples

```text
POST   /api/auth/login
POST   /api/auth/signup
GET    /api/users/me
PATCH  /api/users/me

GET    /api/games
POST   /api/games
GET    /api/games/{game_id}
PATCH  /api/games/{game_id}
POST   /api/games/{game_id}/start
POST   /api/games/{game_id}/pause
POST   /api/games/{game_id}/end
POST   /api/games/{game_id}/events
GET    /api/games/{game_id}/events
GET    /api/games/{game_id}/box-score

GET    /api/teams
POST   /api/teams
GET    /api/teams/{team_id}
PATCH  /api/teams/{team_id}
GET    /api/teams/{team_id}/roster
POST   /api/teams/{team_id}/roster

GET    /api/tournaments
POST   /api/tournaments
POST   /api/tournaments/{tournament_id}/apply

POST   /api/pdf/parse
GET    /api/pdf/templates
POST   /api/pdf/export

POST   /api/payments
POST   /api/credits/recharge
POST   /api/credits/use

POST   /api/hardware/scoreboard/send-packet
```

---

## 10. Logging, Error Handling, and Testing Guidelines

## 10.1 Logging

Logging is mandatory, not optional.

### Actions That Must Be Logged

- Login success and failure
- Permission change
- Team creation, edit, and deletion
- Player data creation, edit, and deletion
- Game creation
- Game start, pause, resume, and end
- Score change
- Foul change
- Timeout change
- Game correction
- PDF upload
- PDF parsing result
- PDF review confirmation
- File download
- Payment success and failure
- Credit recharge and usage
- Point reward
- Sensitive information access
- Hardware packet transmission

### Example Log Fields

```json
{
  "level": "INFO",
  "event": "GAME_SCORE_UPDATED",
  "user_id": "scorekeeper_001",
  "game_id": "game_001",
  "before": { "home": 34, "away": 29 },
  "after": { "home": 34, "away": 31 },
  "timestamp": "2026-05-08T12:00:00+09:00",
  "request_id": "req_abc123"
}
```

---

## 10.2 Defensive Programming

### Mandatory Principles

1. Validate all user input.
2. Do not trust frontend values.
3. Verify permissions again in the backend.
4. Prevent negative scores, negative fouls, and invalid times.
5. Prevent duplicate payments.
6. Prevent duplicate point rewards.
7. Limit file upload type and size.
8. Provide global error handling.
9. Ensure errors do not crash the entire application.

---

## 10.3 Comments and Documentation

### Mandatory Conditions

- Provide JSDoc or equivalent documentation for major frontend functions and components.
- Provide docstrings for major backend functions.
- Document parameter types, return values, and possible errors.
- Explain complex business logic with comments.
- Keep API schemas documented.
- Include a README for setup and deployment.

---

## 10.4 Testing

### Required Test Coverage

- Score calculation
- Foul calculation
- Game clock state transition
- Undo and correction logic
- RBAC permission checks
- PDF parsing fallback to `N/A`
- PDF review confirmation
- File upload validation
- Payment rollback
- Credit balance lock
- Point abuse prevention
- API validation
- Frontend component rendering
- Responsive layout for major screens
- Hardware packet generation

---

## 11. AI Self-development Lifecycle

AI must internally or explicitly follow the following cycle when implementing features.

### 11.1 Plan Alignment

- Identify the relevant section of this document.
- Classify the work as Phase 1 or Phase 2.
- Identify affected domains such as frontend, backend, database, permissions, logging, and tests.
- Define the implementation roadmap.

### 11.2 Implementation and Simulated Run

- Write code.
- Simulate how it behaves in Vue.js and FastAPI.
- Check normal paths and failure paths.
- Verify expected state changes.

### 11.3 Log-based Debugging

- Add logs before and after important operations.
- Predict expected log output.
- Check whether logs are sufficient to diagnose errors.
- Avoid leaking sensitive information in logs.

### 11.4 Retrospective and Validation

Ask questions such as:

- Can elderly users or children operate this UI?
- Does the responsive layout break on mobile?
- Can the API be abused?
- Is permission control enforced in both frontend and backend?
- Can transaction failure corrupt data?
- Are edge cases covered by tests?

### 11.5 Feedback Loop

- Summarize limitations of the implementation.
- List possible bugs or edge cases.
- Suggest next improvements.
- Add a `Self-Reflection` section at the end of AI-generated implementation reports when useful.

---

## 12. Security and Operations Policy

## 12.1 Authentication and Authorization

- Use session-based or token-based authentication.
- Enforce RBAC in both frontend and backend.
- Log permission changes.
- Separate admin APIs from general APIs.
- Protect sensitive APIs against unauthorized access.

## 12.2 File Security

- Validate MIME type.
- Validate extension.
- Limit file size.
- Scan or block suspicious files where possible.
- Store uploaded files outside executable paths.
- Control file download permissions.
- Log file upload and download history.

## 12.3 Payment Security

- Do not store raw card information.
- Verify payment gateway responses.
- Prevent duplicate requests.
- Apply transaction rollback.
- Keep payment audit logs.
- Provide admin review for abnormal transactions.

## 12.4 Personal Data Protection

- Minimize collected personal data.
- Mask or blur sensitive data by permission level.
- Encrypt data where necessary.
- Log sensitive information access.
- Provide deletion or deactivation flow where appropriate.

---

## 13. MVP Priority

## 13.1 Highest Priority Implementation

1. Basic frontend layout
2. Login/signup
3. Role and permission structure
4. Team CRUD
5. Player CRUD
6. Game creation
7. Game control panel
8. Digital score sheet
9. Scoreboard display route
10. Game result screen
11. Basic community board
12. Notices, FAQ, manual
13. Team roster and attendance vote
14. PDF template download
15. Basic PDF export
16. Logging and audit structure

## 13.2 Lower Priority Implementation

1. Advanced PDF AI parsing
2. Gym reservation
3. Payment gateway integration
4. Credit and point system
5. Banner advertising
6. Manner score
7. Kakao AlimTalk and SMS integration
8. Hardware scoreboard integration
9. Advanced statistics dashboard
10. Full-scale mobile app conversion

---

## 14. Definition of Done

### 14.1 Functional Criteria

- Each major feature is connected to a menu or route.
- CRUD features work end to end.
- Permissions are applied in frontend and backend.
- State-changing operations are logged.
- Basic tests exist for core logic.
- Errors are handled without crashing the app.

### 14.2 Scoreboard Criteria

- A game can be created.
- Scores can be entered.
- Scores update automatically on the display route.
- Fouls, timeouts, and clock state can be managed.
- Game results are saved.
- Box scores can be viewed.
- Corrections are logged.

### 14.3 PDF Criteria

- PDF templates can be downloaded.
- Key data can be exported to PDF.
- Uploaded PDFs can be parsed at a basic level.
- Missing values are shown as `N/A`.
- Manual review exists before saving parsed data.

### 14.4 Payment and Credit Criteria

These apply to Phase 2.

- Payment success and failure are handled.
- Credit balance is updated accurately.
- Failed transactions are rolled back.
- Duplicate payment requests are blocked.
- Logs are available for admin review.

---

## 15. Common Confusion Points During Implementation

1. The scoreboard display route and the game control panel are separate screens.
2. The digital score sheet is not just a score input screen; it must also update player statistics.
3. PDF parsing must not directly write finalized data to the database without review.
4. Guest viewing may be open, but writing, editing, downloading, approving, and payment actions require permission.
5. Phase 1 is free MVP; Phase 2 contains payment, credits, advertising, and gym reservation commercialization.
6. External hardware integration is an extension. The web scoreboard must work independently first.
7. Community file uploads require security validation.
8. Team intranet data may include sensitive personal information and must be protected.

---

## 16. Final Development Direction Summary

The first product should be a practical, free, web-based smart scoreboard and amateur basketball management platform that can be used immediately in real games.

The MVP must focus on:

- Easy game control
- Digital scorekeeping
- Team and player data management
- Public community and support pages
- Team roster and attendance management
- PDF export and basic document automation
- Strong logging, permission control, and error handling

Commercial features such as gym reservations, payments, credits, points, advertising, and manner score should be designed as Phase 2 extensions, not mixed into the initial MVP in a way that delays the core service.

---

## 17. Final Instruction to AI Developers

When developing this project, do not simply generate screens one by one.

First understand the service as an amateur basketball operation ecosystem. Then separate the implementation into domain units: game operation, records, team management, community, documents, payments, hardware integration, and operations.

For every generated feature, include:

1. Relevant requirement section
2. Implementation plan
3. Code
4. Logging
5. Error handling
6. Permission rules
7. Test cases
8. Edge cases
9. Self-reflection or next improvement notes when useful

The highest priority is not visual decoration. The highest priority is a reliable field tool that scorekeepers, team managers, and tournament organizers can actually use during real amateur basketball games.

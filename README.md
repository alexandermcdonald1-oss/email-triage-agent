# Email Triage Agent

## Overview

Email Triage Agent is a personal AI-powered email automation project designed to classify incoming emails, determine whether action is required, apply appropriate labels, and generate concise summaries and notifications.

The project is intended to automate inbox management while providing a practical learning platform for AI agents, workflow automation, API integration, and large language model (LLM) applications.

## Objectives

* Automatically classify incoming emails into meaningful categories.
* Identify emails requiring user action.
* Extract important information such as due dates, amounts, and deadlines.
* Apply Gmail labels and organize emails automatically.
* Generate concise summaries of important emails.
* Notify the user of high-priority items.
* Reduce inbox clutter and manual email processing.

## Email Categories

### Property

Property-related communications including:

* Conveyancing
* Real estate transactions
* Property managers
* Mortgage correspondence
* Council notices
* Rates notices
* Legal matters relating to property

### Finance

Financial communications including:

* Bills
* Invoices
* Receipts
* Banking correspondence
* Investments
* Tax matters
* Insurance
* Utilities

### School

School-related communications including:

* Pacific Lutheran College
* School administration
* Excursions
* Sporting activities
* Parent communications
* School fee notices

### ApprovedMods

Business-related communications associated with ApprovedMods including:

* Vehicle modifications
* GVM upgrades
* Engineering certifications
* Vehicle inspections
* Customer enquiries
* Supplier correspondence

### Security

Security-related communications including:

* Login alerts
* Multi-factor authentication notifications
* Password resets
* Fraud alerts
* Account security warnings

### Personal

Personal communications including:

* Family correspondence
* Friends
* Medical appointments
* Travel arrangements
* Social events

### Newsletter

Informational communications including:

* Industry updates
* News digests
* Subscribed newsletters
* Educational content

### Marketing

Promotional communications including:

* Sales
* Discounts
* Advertising
* Product promotions
* Retail offers

### Other

Any email that does not clearly fit into one of the above categories.

---

## Target Workflow

Incoming Email
↓
Retrieve Email
↓
AI Classification
↓
Determine Action Required
↓
Extract Important Information
↓
Apply Gmail Label
↓
Generate Summary
↓
Notify User (if required)

---

## Planned Outputs

For each email, the system will generate:

```json
{
  "category": "Finance",
  "action_required": true,
  "priority": "High",
  "summary": "Electricity bill for $234.50 due 15 June.",
  "due_date": "2026-06-15"
}
```

---

## Project Roadmap

### Phase 1

* OpenAI integration
* Email classification
* Local testing

### Phase 2

* Gmail API integration
* Email retrieval

### Phase 3

* Automatic Gmail label application
* Folder organization

### Phase 4

* Action detection
* Due date extraction
* Financial amount extraction

### Phase 5

* Notifications and reminders
* Apple Reminders integration

### Phase 6

* Agentic workflows
* Automated follow-up recommendations
* Advanced inbox management

---

## Technology Stack

* Python 3.12
* OpenAI API
* Gmail API
* VS Code
* GitHub
* Conda
* Python Dotenv

---

## Purpose

This project serves both as a practical personal productivity tool and as a hands-on learning platform for AI agents, workflow automation, API integrations, and modern LLM-powered applications.

# -*- coding: utf-8 -*-

from openerp import models, fields, api


# class Job(models.Model):
#     _name = 'hr_recruiting.job'
#
#     name = fields.Char(required=True)
#     description = fields.Char()


class JobPosition(models.Model):
    _name = "hr_recruiting.job_position"

    name = fields.Char(required=True)
    description = fields.Text()
    number_of_positions_available = fields.Integer()
    state = fields.Selection([
        ('open', "Position Open"),
        ('closed', "Position Closed"),
    ])

    # application_id= fields.One2many('hr_recruitment.application', string='Applications')

    @api.multi
    def action_open(self):
        self.state = 'open'

    @api.multi
    def action_closed(self):
        self.state = 'closed'


class Applicant(models.Model):
    _name = "hr_recruiting.applicant"

    name = fields.Char(required=True)
    degree_ids = fields.Many2one('hr_recruiting.degree', string="Degree")
    skill_ids = fields.Many2many('hr_recruiting.skill', string="Skill")
    active = fields.Boolean(default=False)
    partner_id = fields.Many2one('res.partner', 'Contact')
    # TODO: Sredi polja!!!

    email_from = fields.Char('Email', size=128, help="These people will receive email.")
    partner_name = fields.Char("Applicant's Name")
    partner_phone = fields.Char('Phone', size=32)
    partner_mobile = fields.Char('Mobile', size=32)

    # TODO: sredi onchange funkciju

    @api.onchange('partner_id')
    def copy_fields(self):
        self.name = self.partner_id.name
        self.email_from = self.partner_id.email
        self.partner_mobile = self.partner_id.mobile
        self.partner_phone = self.partner_id.phone


class Application(models.Model):
    _name = 'hr_recruiting.application'

    # state = fields.Selection([
    #     ('accepted', "Application accepted"),
    #     ('testing', "Testing"),
    #     ('interview', "Interview"),
    #     ('rejected', 'Rejected'),
    #     ('refused', 'Refused'),
    #     ('hired', 'Hired')
    # ])

    active_applicant = fields.Many2one('res.partner', string="Active Applicant",
                                       domain=[('active', '=', True)])

    job_pos_ids = fields.Many2one('hr_recruiting.job_position',
                                  string="Job position",
                                  domain=[('number_of_positions_available', '>', 0)]
                                  )

    interview_date = fields.Date()
    hired = fields.Boolean(default=False)
    number_of_positions = fields.Integer(compute='onchange_job_pos_ids')

    @api.multi  # depends('job_pos_ids')
    def onchange_job_pos_ids(self):
        self.number_of_positions = self.job_pos_ids.number_of_positions_available

    # TODO: Dodaj constraint
    """Ne moze da se sacuva ako nema aplikanta ili posla"""

    """Ne moze ako pozicija nije aktivna"""
    # @api.constrains('job_pos_id', 'open')
    # def _check_job_availability(self):
    #     for record in self:
    #         if record.job_pos_id:
    #             raise exceptions.ValidationError("Position is not open")

    """
    hire_applicant prebacuje stanje u hired

    @api.multi
    def action_hired(self):
        self.state = 'hired'
        self.hired = True
        self.number_of_positions -=1

    """

    """
    Izmeni broj u job position kada aplikant bude hired
    @api.multi
    def _calculate_no_of_job_positions(self):
        pass
    """

    # @api.multi
    # def action_accepted(self):
    #     self.state = 'accepted'
    #
    # @api.multi
    # def action_testing(self):
    #     self.state = 'testing'
    #
    # @api.multi
    # def action_interview(self):
    #     self.state = 'interview'
    #
    # @api.multi
    # def action_refused(self):
    #     self.state='refused'
    #
    # @api.multi
    # def action_rejected(self):
    #     self.state = 'rejected'
    #
    # @api.multi
    # def action_hired(self):
    #     self.state = 'hired'


class Degree(models.Model):
    _name = "hr_recruiting.degree"

    name = fields.Char(string="Degree", required=True)


class Skill(models.Model):
    _name = "hr_recruiting.skill"

    name = fields.Char(string="Skill", required=True)
